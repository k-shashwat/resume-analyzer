import re
from collections import Counter
from typing import Optional, List

from lib.data.skills_ontology import FLAT_SKILLS
from lib.data.domains import get_skills_categories_for_domain
from lib.data.acronyms import expand_terms


def _get_active_skills(domain: Optional[str]) -> List[str]:
    cats = get_skills_categories_for_domain(domain)
    if cats is None:
        return FLAT_SKILLS
    from lib.data.skills_ontology import SKILLS_ONTOLOGY
    filtered = set()
    for cat in cats:
        filtered.update(SKILLS_ONTOLOGY.get(cat, []))
    return sorted(filtered)


def _count_in_text(forms: set[str], text: str) -> int:
    total = 0
    for form in forms:
        if " " in form:
            total += text.count(form)
        else:
            total += len(re.findall(r"\b" + re.escape(form) + r"\b", text))
    return total


def _exists_in_text(forms: set[str], text: str, words_set: set[str]) -> bool:
    for form in forms:
        if " " in form:
            if form in text:
                return True
            form_words = set(form.split())
            if form_words.issubset(words_set):
                return True
        else:
            if re.search(r"\b" + re.escape(form) + r"\b", text):
                return True
    return False


def identify_skill_gaps(resume_text: str, job_description: Optional[str], domain: Optional[str] = None) -> dict:
    if not job_description or not job_description.strip():
        return {
            "score": None,
            "matched_skills": [],
            "missing_skills": [],
            "message": "No job description provided. Skill gap analysis skipped."
        }

    active_skills = _get_active_skills(domain)

    resume_lower = resume_text.lower()
    resume_words = set(re.findall(r"\b[a-z+#.]+\b", resume_lower))
    jd_lower = job_description.lower()

    skill_expansions = {}
    for skill in active_skills:
        skill_expansions[skill] = expand_terms({skill})

    found_in_resume = set()
    for skill in active_skills:
        forms = skill_expansions[skill]
        if _exists_in_text(forms, resume_lower, resume_words):
            found_in_resume.add(skill)

    jd_skill_counts = Counter()
    for skill in active_skills:
        forms = skill_expansions[skill]
        count = _count_in_text(forms, jd_lower)
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
        mentions = jd_skill_counts[skill]
        priority = "high" if mentions >= 3 else "medium" if mentions >= 2 else "low"
        priority_missing.append({
            "skill": skill,
            "mentions_in_jd": mentions,
            "priority": priority,
        })

    suggestions = []
    high_priority = [s for s in priority_missing if s["priority"] == "high"]
    if high_priority:
        skills_list = ", ".join(s["skill"] for s in high_priority[:5])
        suggestions.append(f"Critical skills to add: {skills_list}")

    return {
        "score": match_percentage,
        "matched_skills": [{"skill": s, "mentions_in_jd": jd_skill_counts[s]} for s in matched[:20]],
        "missing_skills": priority_missing,
        "total_required": total_required,
        "matched_count": match_count,
        "missing_count": len(missing),
        "match_percentage": match_percentage,
        "suggestions": suggestions,
    }
