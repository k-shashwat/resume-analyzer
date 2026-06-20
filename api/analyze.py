import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from lib.parser import parse_resume, extract_email, extract_phone
from lib.data.acronyms import add_runtime_groups, reset_runtime_groups, parse_acronyms_from_text, set_domain
from lib.analyzer.ats import score_ats_compatibility
from lib.analyzer.keywords import match_keywords
from lib.analyzer.sections import analyze_sections
from lib.analyzer.verbs import score_verbs_and_quantification
from lib.analyzer.skills import identify_skill_gaps

app = FastAPI(title="ResumeScanner", description="ATS Resume Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_EXTENSIONS = {".pdf", ".docx"}
MAX_JD_LENGTH = 5000


@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "ResumeScanner"}


@app.post("/api/parse")
async def parse_file(file: UploadFile = File(...)):
    if not file.filename:
        return {"error": "No file provided."}

    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return {"error": f"Unsupported file format: {ext}. Please upload a PDF or DOCX file."}

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        return {"error": f"File too large ({len(contents) / 1024 / 1024:.1f}MB). Maximum allowed size is 5MB."}

    try:
        text = parse_resume(contents, file.filename)
    except Exception as e:
        return {"error": f"Failed to parse file: {str(e)}"}

    if not text.strip():
        return {"error": "Could not extract text from the file."}

    if len(text) > MAX_JD_LENGTH:
        text = text[:MAX_JD_LENGTH]

    return {"text": text, "filename": file.filename, "word_count": len(text.split())}


@app.post("/api/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: Optional[str] = Form(None),
    domain: Optional[str] = Form(None),
):
    if not file.filename:
        return {"error": "No file provided."}

    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return {
            "error": f"Unsupported file format: {ext}. Please upload a PDF or DOCX file.",
            "supported_formats": list(ALLOWED_EXTENSIONS),
        }

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        return {
            "error": f"File too large ({len(contents) / 1024 / 1024:.1f}MB). Maximum allowed size is 5MB.",
            "max_size_mb": 5,
        }

    try:
        text = parse_resume(contents, file.filename)
    except Exception as e:
        return {"error": f"Failed to parse file: {str(e)}"}

    if not text.strip():
        return {"error": "Could not extract text from the file. The PDF may be image-based or corrupted."}

    if job_description and len(job_description) > MAX_JD_LENGTH:
        job_description = job_description[:MAX_JD_LENGTH]

    if job_description and job_description.strip():
        add_runtime_groups(parse_acronyms_from_text(job_description))

    set_domain(domain)

    ats = score_ats_compatibility(text, contents, file.filename)
    sections = analyze_sections(text, has_contact_info=bool(extract_email(text) or extract_phone(text)))
    verbs = score_verbs_and_quantification(text)
    keywords = match_keywords(text, job_description)
    skills = identify_skill_gaps(text, job_description, domain=domain)

    reset_runtime_groups()

    dimensions = [
        {"name": "ATS Compatibility", "key": "ats", "score": ats["score"], "max": 100},
        {"name": "Sections", "key": "sections", "score": sections["score"], "max": 100},
        {"name": "Action Verbs", "key": "verbs", "score": verbs["score"], "max": 100},
    ]

    if keywords["match_percentage"] is not None:
        dimensions.append({"name": "Keyword Match", "key": "keywords", "score": keywords["score"], "max": 100})
    if skills["score"] is not None:
        dimensions.append({"name": "Skill Match", "key": "skills", "score": skills["score"], "max": 100})

    valid_scores = [d["score"] for d in dimensions if d["score"] is not None]
    overall = round(sum(valid_scores) / len(valid_scores)) if valid_scores else 0

    return {
        "overall_score": overall,
        "dimensions": dimensions,
        "ats": ats,
        "sections": sections,
        "verbs": verbs,
        "keywords": keywords,
        "skills": skills,
        "metadata": {
            "filename": file.filename,
            "text_length": len(text),
            "word_count": len(text.split()),
        }
    }
