import pytest
from lib.analyzer.ats import score_ats_compatibility


SAMPLE_TEXT = """John Doe
john@example.com
(555) 123-4567

Summary
Experienced software engineer with 5 years of full-stack development experience.

Experience
Software Engineer, Tech Corp
2020 - Present
- Led development of microservices platform
- Reduced latency by 40% through caching optimization

Education
BS Computer Science, University of Technology

Skills
Python, React, TypeScript, AWS, Docker
"""


def test_returns_score():
    result = score_ats_compatibility(
        SAMPLE_TEXT,
        b"test",
        "resume.docx",
    )
    assert 0 <= result["score"] <= 100


def test_returns_issues():
    result = score_ats_compatibility(
        SAMPLE_TEXT,
        b"test",
        "resume.docx",
    )
    assert isinstance(result["issues"], list)


def test_has_email_and_phone():
    result = score_ats_compatibility(
        SAMPLE_TEXT,
        b"test",
        "resume.docx",
    )
    assert result["details"]["has_email"] is True
    assert result["details"]["has_phone"] is True


def test_empty_text_scores_zero():
    result = score_ats_compatibility(
        "",
        b"",
        "empty.pdf",
    )
    assert result["score"] == 0
    assert len(result["issues"]) > 0


def test_returns_details():
    result = score_ats_compatibility(
        SAMPLE_TEXT,
        b"test",
        "resume.docx",
    )
    assert "pages" in result["details"]
    assert "word_count" in result["details"]
