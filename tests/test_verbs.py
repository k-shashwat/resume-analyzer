import pytest
from lib.analyzer.verbs import score_verbs_and_quantification


SAMPLE_WITH_VERBS_AND_QUANT = """Experience

- Led a team of 12 engineers across 3 product teams
- Increased revenue by 35% through strategic partnerships
- Reduced infrastructure costs by $500,000 annually
- Developed a new CI/CD pipeline serving 200+ developers
- Managed $2M budget and delivered 15% under budget
- Built and deployed microservices architecture handling 1M+ requests/day
"""

SAMPLE_WEAK = """Experience

- Was responsible for some things at the company
- Helped with various projects and tasks
- Worked on the website and did some updates
- Assisted team members with their daily work
"""


def test_finds_action_verbs():
    result = score_verbs_and_quantification(SAMPLE_WITH_VERBS_AND_QUANT)
    assert result["verb_count"] > 3
    verbs = result["found_action_verbs"]
    assert "led" in verbs
    assert "increased" in verbs or "increase" in verbs


def test_finds_quantification():
    result = score_verbs_and_quantification(SAMPLE_WITH_VERBS_AND_QUANT)
    assert result["quantified_bullet_count"] >= 3


def test_weak_bullets_score_low():
    result = score_verbs_and_quantification(SAMPLE_WEAK)
    assert result["verb_score"] < 50
    assert result["quantification_score"] == 0


def test_score_range():
    result = score_verbs_and_quantification(SAMPLE_WITH_VERBS_AND_QUANT)
    assert 0 <= result["score"] <= 100
    assert 0 <= result["verb_score"] <= 100
    assert 0 <= result["quantification_score"] <= 100


def test_issues_for_weak_bullets():
    result = score_verbs_and_quantification(SAMPLE_WEAK)
    assert len(result["issues"]) > 0


def test_suggestions_for_weak_bullets():
    result = score_verbs_and_quantification(SAMPLE_WEAK)
    assert len(result["suggestions"]) > 0
