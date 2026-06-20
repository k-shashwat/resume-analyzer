from lib.data.section_headers import SECTION_MAPPING, CANONICAL_NAMES, SECTIONS_EXPECTED, SECTIONS_OPTIONAL


def _levenshtein(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return _levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev[j + 1] + 1
            deletions = curr[j] + 1
            substitutions = prev[j] + (c1 != c2)
            curr.append(min(insertions, deletions, substitutions))
        prev = curr
    return prev[-1]


def analyze_sections(text: str, has_contact_info: bool = False) -> dict:
    lines = text.split("\n")
    found_sections = {}
    section_order = []

    for i, line in enumerate(lines):
        stripped = line.strip().lower()
        cleaned = "".join(c for c in stripped if c.isalnum() or c.isspace())
        if len(cleaned) < 3 or len(cleaned) > 60:
            continue

        best_match = None
        best_dist = float("inf")

        for canonical, variants in SECTION_MAPPING.items():
            for variant in variants:
                dist = _levenshtein(cleaned, variant)
                if dist <= 2 and dist < best_dist:
                    best_dist = dist
                    best_match = canonical

        if best_match and best_match not in found_sections:
            found_sections[best_match] = {
                "line_number": i + 1,
                "matched_text": line.strip(),
                "canonical_name": CANONICAL_NAMES.get(best_match, best_match),
                "section_type": "expected" if best_match in SECTIONS_EXPECTED else "optional",
            }
            section_order.append(best_match)

    if has_contact_info and "contact" not in found_sections:
        found_sections["contact"] = {
            "line_number": 0,
            "matched_text": "(detected via email/phone)",
            "canonical_name": "Contact",
            "section_type": "expected",
        }
        section_order.insert(0, "contact")

    found_expected = [s for s in SECTIONS_EXPECTED if s in found_sections]
    missing_expected = [s for s in SECTIONS_EXPECTED if s not in found_sections]
    found_optional = [s for s in SECTIONS_OPTIONAL if s in found_sections]

    score = round(len(found_expected) / len(SECTIONS_EXPECTED) * 100)

    issues = []
    for section in missing_expected:
        issues.append({
            "severity": "high" if section in ("experience", "education") else "medium",
            "section": CANONICAL_NAMES.get(section, section),
            "message": f"Missing '{CANONICAL_NAMES.get(section, section)}' section. This is a critical section for most ATS systems.",
        })

    bonus = len(found_optional) * 2

    return {
        "score": min(100, score + bonus),
        "found_sections": {s: found_sections[s] for s in section_order},
        "missing_sections": [CANONICAL_NAMES.get(s, s) for s in missing_expected],
        "bonus_sections": [CANONICAL_NAMES.get(s, s) for s in found_optional],
        "issues": issues,
        "details": {
            "expected_total": len(SECTIONS_EXPECTED),
            "expected_found": len(found_expected),
            "optional_found": len(found_optional),
        }
    }
