import pytest
from lib.analyzer.sections import analyze_sections, _levenshtein


def test_levenshtein():
    assert _levenshtein("abc", "abc") == 0
    assert _levenshtein("abc", "abd") == 1
    assert _levenshtein("kitten", "sitting") == 3
    assert _levenshtein("", "abc") == 3
    assert _levenshtein("abc", "") == 3


SAMPLE_RESUME = """John Doe

SUMMARY
Experienced software engineer with 8 years of experience.

EXPERIENCE
Senior Software Engineer, Tech Corp
Jan 2020 - Present
- Led team of 5 engineers

EDUCATION
BS Computer Science, University of Technology, 2015

SKILLS
Python, JavaScript, React, AWS
"""


def test_find_expected_sections():
    result = analyze_sections(SAMPLE_RESUME)
    sections = result["found_sections"]
    section_names = list(sections.keys())

    assert "summary" in section_names
    assert "experience" in section_names
    assert "education" in section_names
    assert "skills" in section_names


def test_score_range():
    result = analyze_sections(SAMPLE_RESUME)
    assert 0 <= result["score"] <= 100


def test_missing_sections():
    result = analyze_sections("""Name
email@test.com

EXPERIENCE
Software Engineer, 2020-2023
""")
    missing = result["missing_sections"]
    assert len(missing) > 0


def test_fuzzy_matching():
    result = analyze_sections("""Resume

WORK EXPIRIENCE
Did stuff

EDUCATIN
School info

Profesional Summary
Overview text
""")
    sections = result["found_sections"]
    assert "experience" in sections
    assert "education" in sections


def test_bonus_sections():
    result = analyze_sections("""Resume

SUMMARY
Overview

EXPERIENCE
Work

EDUCATION
School

SKILLS
Languages

PROJECTS
Some projects

CERTIFICATIONS
AWS Certified
""")
    assert len(result["bonus_sections"]) >= 2
    assert result["score"] > 0
