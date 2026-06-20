import re
from collections import Counter
from typing import Optional

import spacy

from lib.data.acronyms import expand_terms
from lib.data.word_weights import term_specificity_score, get_word_idf, DEFAULT_IDF

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
              "if", "now", "well", "etc",
              "high", "low", "large", "small", "able", "new", "old",
              "good", "better", "best", "potential", "key", "plus",
              "role", "part", "team", "set", "use", "need", "way",
              "lot", "bit"}


MIN_TERM_LENGTH = 3

def _extract_noun_phrases(text: str) -> set:
    nlp_obj = _get_nlp()
    doc = nlp_obj(text)
    phrases = set()
    tokens = list(doc)
    i = 0
    while i < len(tokens):
        token = tokens[i]
        lemma = token.lemma_.lower()
        if token.pos_ in ("NOUN", "PROPN", "ADJ") and lemma not in STOP_WORDS and len(lemma) >= MIN_TERM_LENGTH:
            phrase = [lemma]
            j = i + 1
            while j < len(tokens) and tokens[j].pos_ in ("NOUN", "PROPN", "ADJ") and tokens[j].lemma_.lower() not in STOP_WORDS and len(tokens[j].lemma_) >= MIN_TERM_LENGTH:
                phrase.append(tokens[j].lemma_.lower())
                j += 1
            if 2 <= len(phrase) <= 3:
                phrase_str = " ".join(phrase)
                if any(get_word_idf(w) >= 5.0 for w in phrase):
                    phrases.add(phrase_str)
            i = j
        else:
            i += 1
    return phrases


def _extract_noun_chunks(text: str) -> set:
    nlp_obj = _get_nlp()
    doc = nlp_obj(text)
    phrases = set()
    for chunk in doc.noun_chunks:
        cleaned = chunk.text.strip()
        words_count = len(cleaned.split())
        if words_count < 2 or words_count > 3:
            continue
        words = [t.lemma_.lower() for t in chunk
                 if t.pos_ in ("NOUN", "PROPN", "ADJ")
                 and len(t.lemma_) >= MIN_TERM_LENGTH]
        if len(words) < 2:
            continue
        if all(get_word_idf(w) < 5.0 for w in words):
            continue
        phrases.add(" ".join(words))
    return phrases


def _extract_single_keywords(text: str) -> dict[str, int]:
    nlp_obj = _get_nlp()
    doc = nlp_obj(text)
    freq = Counter()
    for token in doc:
        lemma = token.lemma_.lower()
        if (token.pos_ in ("NOUN", "PROPN", "ADJ")
                and lemma not in STOP_WORDS
                and len(lemma) >= MIN_TERM_LENGTH):
            freq[lemma] += 1
    return dict(freq)


def _deduplicate_acronyms(terms: set[str]) -> set[str]:
    expanded = expand_terms(terms)
    deduped = set()
    consumed = set()
    for term in sorted(expanded, key=lambda t: (-len(t), t)):
        if term in consumed:
            continue
        deduped.add(term)
        equivalents = expand_terms({term})
        consumed |= equivalents
    return deduped


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

    jd_phrases = _extract_noun_phrases(job_description)
    jd_chunks = _extract_noun_chunks(job_description)
    jd_multi = jd_phrases | jd_chunks

    jd_singles = _extract_single_keywords(job_description)

    candidates: list[tuple[str, float]] = []

    for term in jd_multi:
        if not term or len(term) < 5:
            continue
        words = term.split()
        if len(words) < 2 or len(words) > 4:
            continue
        freq = 1
        for w in words:
            freq = max(freq, jd_singles.get(w, 1))
        score = freq * term_specificity_score(term)
        candidates.append((term, score))

    for term, freq in jd_singles.items():
        if freq >= 2 and len(term) >= 4:
            score = freq * term_specificity_score(term)
            if score >= 6.0:
                candidates.append((term, score))

    candidates.sort(key=lambda x: -x[1])

    seen_terms: set[str] = set()
    ranked: list[str] = []
    for term, score in candidates:
        if score < 6.0 and len(ranked) >= 5:
            continue
        if score < 5.5 and len(ranked) >= 15:
            continue
        if score < 5.0:
            continue
        term_key = term.lower()
        if term_key in seen_terms:
            continue
        expanded = expand_terms({term_key})
        skip = False
        for existing in seen_terms:
            if expand_terms({existing}) & expanded:
                skip = True
                break
        if skip:
            continue
        ranked.append(term)
        seen_terms.add(term_key)
        seen_terms |= expanded

    jd_terms = set(ranked)
    jd_terms = _deduplicate_acronyms(jd_terms)

    resume_lower = resume_text.lower()
    resume_words = set(re.findall(r"\b[a-z+#.]+\b", resume_lower))

    nlp_obj = _get_nlp()
    resume_doc = nlp_obj(resume_lower)
    resume_lemmas = {t.lemma_.lower() for t in resume_doc if len(t.lemma_) > 1}
    resume_lookup = resume_words | resume_lemmas

    jd_expanded_lookup = {}
    for jd_term in jd_terms:
        jd_expanded_lookup[jd_term] = expand_terms({jd_term})

    matched = []
    missing = []

    for jd_term in sorted(jd_terms):
        if not jd_term or len(jd_term) < 2:
            continue
        expanded_forms = jd_expanded_lookup.get(jd_term, {jd_term})
        is_match = False
        for form in expanded_forms:
            if " " in form:
                if form in resume_lower:
                    is_match = True
                    break
                form_words = set(form.split())
                if form_words.issubset(resume_lookup):
                    is_match = True
                    break
            else:
                if form in resume_lookup:
                    is_match = True
                    break
        if is_match:
            matched.append({"keyword": jd_term, "type": "phrase" if " " in jd_term else "single"})
        else:
            missing.append({"keyword": jd_term, "type": "phrase" if " " in jd_term else "single"})

    total = len(jd_terms)
    match_percentage = round(len(matched) / total * 100) if total > 0 else 0

    return {
        "score": match_percentage,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "total_keywords": total,
        "matched_count": len(matched),
        "missing_count": len(missing),
        "match_percentage": match_percentage,
    }
