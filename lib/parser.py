import io
import re
from typing import Optional

import pdfplumber
from pdfplumber.utils.exceptions import PdfminerException
from docx import Document


def _words_to_lines(words: list[dict]) -> str:
    if not words:
        return ""
    lines: list[list[dict]] = []
    sorted_words = sorted(words, key=lambda w: (round(w["top"], 0), w["x0"]))
    current_line = [sorted_words[0]]
    for w in sorted_words[1:]:
        if abs(w["top"] - current_line[-1]["top"]) <= 3:
            current_line.append(w)
        else:
            lines.append(current_line)
            current_line = [w]
    if current_line:
        lines.append(current_line)
    output_lines: list[str] = []
    for line_words in lines:
        line_words.sort(key=lambda w: w["x0"])
        output_lines.append(" ".join(w["text"] for w in line_words))
    return "\n".join(output_lines)


def parse_pdf(file_bytes: bytes) -> str:
    try:
        page_texts: list[str] = []
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                words = page.extract_words()
                line_text = _words_to_lines(words)
                if line_text:
                    page_texts.append(line_text)
        text = "\n".join(page_texts)
        text = re.sub(r"[^\S\n]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() if text.strip() else ""
    except PdfminerException:
        return ""


def parse_docx(file_bytes: bytes) -> str:
    doc = Document(io.BytesIO(file_bytes))
    paragraphs = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            paragraphs.append(text)
    for table in doc.tables:
        for row in table.rows:
            row_text = " ".join(cell.text.strip() for cell in row.cells if cell.text.strip())
            if row_text:
                paragraphs.append(row_text)
    return "\n".join(paragraphs)


def parse_resume(file_bytes: bytes, filename: str) -> str:
    filename_lower = filename.lower()
    if filename_lower.endswith(".pdf"):
        return parse_pdf(file_bytes)
    elif filename_lower.endswith(".docx"):
        return parse_docx(file_bytes)
    else:
        raise ValueError(f"Unsupported file format: {filename}. Expected PDF or DOCX.")


def extract_email(text: str) -> Optional[str]:
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None


def extract_phone(text: str) -> Optional[str]:
    patterns = [
        r"\+\d{1,3}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}",
        r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(0).strip()
    return None


def has_images(file_bytes: bytes, filename: str) -> bool:
    if not filename.lower().endswith(".pdf"):
        return False
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                if page.images:
                    return True
    except PdfminerException:
        return False
    return False


def count_pages(file_bytes: bytes, filename: str) -> int:
    if filename.lower().endswith(".pdf"):
        try:
            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                return len(pdf.pages)
        except PdfminerException:
            return 1
    return 1


def has_tables(file_bytes: bytes, filename: str) -> bool:
    if not filename.lower().endswith(".pdf"):
        return False
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                if page.find_tables():
                    return True
    except PdfminerException:
        return False
    return False


def has_columns(file_bytes: bytes, filename: str) -> bool:
    if not filename.lower().endswith(".pdf"):
        return False
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                chars = page.chars
                if not chars:
                    continue
                x_positions = sorted(set(round(c["x0"]) for c in chars))
                distinct_columns = 1
                for i in range(1, len(x_positions)):
                    if x_positions[i] - x_positions[i - 1] > 50:
                        distinct_columns += 1
                if distinct_columns > 2:
                    return True
    except PdfminerException:
        return False
    return False


def count_words(text: str) -> int:
    return len(text.split())
