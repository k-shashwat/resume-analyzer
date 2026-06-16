from typing import Optional

from lib.parser import extract_email, extract_phone, has_images, count_pages, has_tables, has_columns, count_words


def score_ats_compatibility(
    text: str,
    file_bytes: bytes,
    filename: str,
) -> dict:
    score = 100
    issues = []

    if not text.strip():
        return {
            "score": 0,
            "issues": [{"severity": "high", "message": "Unable to extract text from file. The PDF may be image-based or corrupted."}],
        }

    pages = count_pages(file_bytes, filename)
    if pages > 2:
        deduction = min(15, (pages - 2) * 5)
        score -= deduction
        issues.append({
            "severity": "medium",
            "message": f"Resume is {pages} pages long. ATS systems prefer 1-2 page resumes. Consider condensing."
        })

    if has_images(file_bytes, filename):
        score -= 15
        issues.append({
            "severity": "high",
            "message": "PDF contains images. ATS may not be able to scan image-based content."
        })

    if has_tables(file_bytes, filename):
        score -= 10
        issues.append({
            "severity": "medium",
            "message": "PDF contains tables. ATS often misreads table layouts. Use simple text formatting."
        })

    if has_columns(file_bytes, filename):
        score -= 10
        issues.append({
            "severity": "medium",
            "message": "Multi-column layout detected. ATS may read columns out of order. Use single-column layout."
        })

    email = extract_email(text)
    if not email:
        score -= 15
        issues.append({
            "severity": "high",
            "message": "No email address found. Contact information is critical for ATS."
        })

    phone = extract_phone(text)
    if not phone:
        score -= 5
        issues.append({
            "severity": "low",
            "message": "No phone number found. Consider adding one."
        })

    words = count_words(text)
    if words < 100:
        score -= 20
        issues.append({
            "severity": "high",
            "message": f"Resume has only {words} words. Content appears too sparse."
        })
    elif words < 250:
        score -= 5
        issues.append({
            "severity": "low",
            "message": f"Resume has {words} words. Consider adding more detail."
        })

    special_chars = sum(1 for c in text if ord(c) > 127 and c not in "\u2013\u2014\u2018\u2019\u201c\u201d\u2022\u2026\u00b0")
    if special_chars > 20:
        score -= 5
        issues.append({
            "severity": "low",
            "message": "Special characters detected. Some may not parse correctly in ATS."
        })

    score = max(0, score)

    return {
        "score": score,
        "issues": issues,
        "details": {
            "pages": pages,
            "has_images": has_images(file_bytes, filename),
            "has_tables": has_tables(file_bytes, filename),
            "has_columns": has_columns(file_bytes, filename),
            "has_email": bool(extract_email(text)),
            "has_phone": bool(extract_phone(text)),
            "word_count": count_words(text),
            "special_char_count": special_chars,
        }
    }
