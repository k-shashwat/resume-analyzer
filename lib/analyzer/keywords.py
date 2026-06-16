import re
from typing import Optional

import spacy

nlp = None

def _get_nlp():
    global nlp
    if nlp is None:
        nlp = spacy.load("en_core_web_sm")
    return nlp


STOP_WORDS = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
              "of", "with", "by", "from", "as", "is", "was", "are", "were", "be",
              "been", "being", "have", "has", "had", "do", "does", "did", "will",
              "would", "could", "should", "may", "might", "can", "shall", "you",
              "your", "we", "our", "they", "their", "it", "its", "this", "that",
              "these", "those", "am", "not", "no", "than", "then", "also", "very",
              "just", "about", "into", "over", "after", "before", "between",
              "through", "during", "without", "within", "along", "among",
              "such", "each", "all", "any", "both", "few", "more", "most",
              "other", "some", "only", "own", "same", "so", "up", "out",
              "if", "now", "well", "etc"}


def _extract_keywords(text: str) -> set:
    nlp_obj = _get_nlp()
    doc = nlp_obj(text.lower())
    keywords = set()

    i = 0
    tokens = list(doc)
    while i < len(tokens):
        token = tokens[i]
        if token.pos_ in ("NOUN", "PROPN", "ADJ") and token.lemma_ not in STOP_WORDS and len(token.lemma_) > 1:
            phrase = [token.lemma_]
            j = i + 1
            while j < len(tokens) and tokens[j].pos_ in ("NOUN", "PROPN", "ADJ") and len(tokens[j].lemma_) > 1:
                phrase.append(tokens[j].lemma_)
                j += 1
            keywords.add(" ".join(phrase))
            i = j
        else:
            i += 1

    keywords.update(
        token.lemma_ for token in doc
        if token.pos_ in ("NOUN", "PROPN", "VERB")
        and token.lemma_ not in STOP_WORDS
        and len(token.lemma_) > 1
    )

    return keywords


def _extract_multi_word_phrases(text: str) -> set:
    nlp_obj = _get_nlp()
    doc = nlp_obj(text.lower())
    phrases = set()

    for chunk in doc.noun_chunks:
        cleaned = chunk.text.strip()
        if len(cleaned.split()) >= 2:
            words = [t.lemma_ for t in chunk if t.pos_ in ("NOUN", "PROPN", "ADJ")]
            if len(words) >= 2:
                phrases.add(" ".join(words))

    return phrases


def match_keywords(resume_text: str, job_description: Optional[str]) -> dict:
    if not job_description or not job_description.strip():
        return {
            "score": None,
            "matched_keywords": [],
            "missing_keywords": [],
            "total_keywords": 0,
            "match_percentage": None,
            "message": "No job description provided. Keyword matching skipped."
        }

    jd_keywords = _extract_keywords(job_description)
    jd_phrases = _extract_multi_word_phrases(job_description)

    all_jd_terms = jd_keywords | jd_phrases

    resume_lower = resume_text.lower()
    resume_words = set(re.findall(r"\b[a-z]+\b", resume_lower))

    nlp_obj = _get_nlp()
    resume_doc = nlp_obj(resume_lower)
    resume_lemmas = {t.lemma_ for t in resume_doc if len(t.lemma_) > 1}

    matched = []
    missing = []

    for term in sorted(all_jd_terms):
        if not term or len(term) < 2:
            continue
        term_lower = term.lower()

        if " " in term:
            if term_lower in resume_lower:
                matched.append({"keyword": term, "type": "phrase"})
                continue
            term_words = set(term.split())
            if term_words.issubset(resume_words):
                matched.append({"keyword": term, "type": "phrase"})
                continue
        else:
            if term_lower in resume_lemmas or term_lower in resume_words:
                matched.append({"keyword": term, "type": "single"})
                continue

        missing.append({"keyword": term, "type": "phrase" if " " in term else "single"})

    total = len(all_jd_terms)
    match_percentage = round(len(matched) / total * 100) if total > 0 else 0

    score = match_percentage

    return {
        "score": score,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "total_keywords": total,
        "matched_count": len(matched),
        "missing_count": len(missing),
        "match_percentage": match_percentage,
    }
