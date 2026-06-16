import pytest
from lib.analyzer.skills import identify_skill_gaps


RESUME_TEXT = """Full-stack developer with expertise in React, Node.js, TypeScript,
PostgreSQL, and AWS. Built REST APIs using Express and NestJS. Deployed
applications on Docker and Kubernetes."""

JD_TEXT = """Looking for a Senior Full-Stack Developer with 5+ years of experience
in React, TypeScript, Node.js, Python, Go, PostgreSQL, MongoDB, AWS, Docker,
Kubernetes, Terraform, CI/CD, GraphQL, and Redis."""


def test_finds_matched_skills():
    result = identify_skill_gaps(RESUME_TEXT, JD_TEXT)
    matched = [m["skill"] for m in result["matched_skills"]]
    assert "React" in matched
    assert "TypeScript" in matched
    assert "PostgreSQL" in matched
    assert "Docker" in matched


def test_finds_missing_skills():
    result = identify_skill_gaps(RESUME_TEXT, JD_TEXT)
    missing = [m["skill"] for m in result["missing_skills"]]
    assert "Python" in missing or any("Python" in s["skill"] for s in result["missing_skills"])
    assert len(missing) > 0


def test_no_jd_returns_none():
    result = identify_skill_gaps(RESUME_TEXT, None)
    assert result["score"] is None
    assert result["message"] is not None


def test_empty_jd_returns_none():
    result = identify_skill_gaps(RESUME_TEXT, "")
    assert result["score"] is None


def test_match_percentage():
    result = identify_skill_gaps(RESUME_TEXT, JD_TEXT)
    assert result["total_required"] > 0
    assert 0 <= result["match_percentage"] <= 100
    assert result["score"] == result["match_percentage"]


def test_prioritizes_missing():
    result = identify_skill_gaps(RESUME_TEXT, JD_TEXT)
    for skill in result["missing_skills"]:
        assert skill["priority"] in ("high", "medium", "low")
        assert "mentions_in_jd" in skill


def test_suggestions():
    result = identify_skill_gaps(RESUME_TEXT, JD_TEXT)
    if any(s["priority"] == "high" for s in result["missing_skills"]):
        assert len(result["suggestions"]) > 0
