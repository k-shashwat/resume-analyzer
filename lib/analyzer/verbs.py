import re
from collections import Counter

import spacy

from lib.data.action_verbs import FLAT_ACTION_VERBS, QUANTIFICATION_PATTERNS

nlp = None

def _get_nlp():
    global nlp
    if nlp is None:
        nlp = spacy.load("en_core_web_sm")
    return nlp


BULLET_MARKERS = re.compile(r"^[\s•\-\*\▸\▪\◦\‣\⦁\⏺\u2013\u2014]+")


def _extract_bullet_points(text: str) -> list:
    lines = text.split("\n")
    bullets = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if BULLET_MARKERS.match(stripped):
            cleaned = BULLET_MARKERS.sub("", stripped).strip()
            if cleaned:
                bullets.append(cleaned)
        elif stripped[0].isalpha() and len(stripped.split()) >= 3:
            first_word = stripped.split()[0].lower()
            if first_word in FLAT_ACTION_VERBS:
                bullets.append(stripped)
    return bullets


def score_verbs_and_quantification(text: str) -> dict:
    nlp_obj = _get_nlp()
    text_lower = text.lower()
    doc = nlp_obj(text_lower)

    text_tokens = {t.text for t in doc}
    text_lemmas = {t.lemma_ for t in doc}
    text_lookup = text_tokens | text_lemmas
    found_verbs = sorted(set(
        v for v in FLAT_ACTION_VERBS if v in text_lookup
    ))

    verb_count = len(found_verbs)
    total_words = len(text.split())

    verb_density = verb_count / max(total_words, 1) * 1000

    bullets = _extract_bullet_points(text)
    bullet_count = len(bullets)

    quantified_bullets = []
    for bullet in bullets:
        for pattern in QUANTIFICATION_PATTERNS:
            if re.search(pattern, bullet, re.IGNORECASE):
                quantified_bullets.append({
                    "text": bullet[:150],
                    "matched_pattern": pattern,
                })
                break

    quant_count = len(quantified_bullets)

    verb_score = min(100, int(verb_count / 15 * 100)) if verb_count < 15 else 100

    quant_score = 0
    if bullet_count > 0:
        quant_ratio = quant_count / bullet_count
        quant_score = min(100, int(quant_ratio / 0.5 * 100))
    elif quant_count > 0:
        quant_score = min(100, quant_count * 10)

    overall_score = int(verb_score * 0.6 + quant_score * 0.4)

    issues = []
    suggestions = []

    if verb_count < 10:
        issues.append({
            "severity": "medium",
            "message": f"Only {verb_count} strong action verbs found. Aim for 15-20 strong action verbs across your resume.",
        })
        suggestions.append("Start each bullet point with a strong action verb like 'Led', 'Developed', 'Optimized'.")

    if quant_count == 0:
        issues.append({
            "severity": "high",
            "message": "No quantifiable achievements found. Add numbers, percentages, or metrics to demonstrate impact.",
        })
        suggestions.append("Add metrics: 'Increased revenue by 30%', 'Managed a team of 12', 'Reduced costs by $50,000'.")
    elif bullet_count > 0 and quant_count / bullet_count < 0.3:
        issues.append({
            "severity": "medium",
            "message": f"Only {quant_count} of {bullet_count} bullet points ({int(quant_count/bullet_count*100)}%) contain quantifiable results. Aim for 50%+.",
        })
        suggestions.append("Add more numbers: time saved, revenue grown, team size, budget managed, percentage improvements.")

    repeated = [v for v, c in Counter(found_verbs).items() if c > 1]
    if repeated:
        issues.append({
            "severity": "low",
            "message": f"Action verbs used multiple times: {', '.join(repeated[:5])}. Vary your language.",
        })
        suggestions.append("Use a thesaurus to find synonyms for repeated action verbs.")

    return {
        "score": overall_score,
        "verb_score": verb_score,
        "quantification_score": quant_score,
        "found_action_verbs": found_verbs,
        "verb_count": verb_count,
        "bullet_count": bullet_count,
        "quantified_bullet_count": quant_count,
        "quantified_examples": quantified_bullets[:5],
        "issues": issues,
        "suggestions": suggestions,
        "details": {
            "verb_density": round(verb_density, 1),
            "quantification_rate": round(quant_count / max(bullet_count, 1) * 100, 1),
        }
    }
