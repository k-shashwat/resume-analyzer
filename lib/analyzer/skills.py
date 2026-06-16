import re
from collections import Counter
from typing import Optional

from lib.data.skills_ontology import FLAT_SKILLS, SKILLS_LOWER


def identify_skill_gaps(resume_text: str, job_description: Optional[str]) -> dict:
    if not job_description or not job_description.strip():
        return {
            "score": None,
            "matched_skills": [],
            "missing_skills": [],
            "message": "No job description provided. Skill gap analysis skipped."
        }

    resume_lower = resume_text.lower()

    found_in_resume = set()
    for skill in FLAT_SKILLS:
        skill_lower = skill.lower()
        if skill_lower in resume_lower:
            found_in_resume.add(skill)
        elif " " in skill:
            words = set(skill_lower.split())
            if words.issubset(set(re.findall(r"\b[a-z+#.]+\b", resume_lower))):
                found_in_resume.add(skill)

    jd_lower = job_description.lower()
    jd_skill_counts = Counter()
    for skill in FLAT_SKILLS:
        skill_lower = skill.lower()
        count = len(re.findall(re.escape(skill_lower), jd_lower))
        if count > 0:
            jd_skill_counts[skill] = count

    required_skills = sorted(jd_skill_counts.keys(), key=lambda s: -jd_skill_counts[s])
    matched = sorted(found_in_resume & set(required_skills), key=lambda s: -jd_skill_counts[s])
    missing = [s for s in required_skills if s not in found_in_resume]

    total_required = len(required_skills)
    match_count = len(matched)
    match_percentage = round(match_count / total_required * 100) if total_required > 0 else 0

    priority_missing = []
    for skill in missing:
        priority = "high" if jd_skill_counts[skill] >= 3 else "medium" if jd_skill_counts[skill] >= 2 else "low"
        priority_missing.append({
            "skill": skill,
            "mentions_in_jd": jd_skill_counts[skill],
            "priority": priority,
        })

    suggestions = []
    high_priority = [s for s in priority_missing if s["priority"] == "high"]
    if high_priority:
        skills_list = ", ".join(s["skill"] for s in high_priority[:5])
        suggestions.append(f"Critical skills to add: {skills_list}")

    score = match_percentage

    return {
        "score": score,
        "matched_skills": [{"skill": s, "mentions_in_jd": jd_skill_counts[s]} for s in matched[:20]],
        "missing_skills": priority_missing,
        "total_required": total_required,
        "matched_count": match_count,
        "missing_count": len(missing),
        "match_percentage": match_percentage,
        "suggestions": suggestions,
    }
