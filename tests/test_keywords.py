import pytest
from lib.analyzer.keywords import match_keywords


RESUME_TEXT = """Experienced Python developer with strong background in React,
Docker, PostgreSQL, and AWS. Led multiple projects using Django and FastAPI.
Implemented CI/CD pipelines with Jenkins and GitHub Actions."""

JD_TEXT = """We are looking for a Senior Python Developer with strong Python
skills and experience in React, Django, PostgreSQL, AWS, Docker. The role
requires Python expertise, Docker containerization, React frontend work,
PostgreSQL database management, and AWS cloud experience. CI/CD, Jenkins,
and microservices knowledge is required. Knowledge of TypeScript and
GraphQL is a plus."""


def test_matches_keywords():
    result = match_keywords(RESUME_TEXT, JD_TEXT)
    matched = [m["keyword"].lower() for m in result["matched_keywords"]]
    assert "python" in matched
    assert any(t in matched for t in ["react", "reactjs", "react js"])
    assert any(t in matched for t in ["docker", "docker container"])
    assert "postgresql" in matched


def test_finds_missing_keywords():
    result = match_keywords(RESUME_TEXT, JD_TEXT)
    missing = [m["keyword"].lower() for m in result["missing_keywords"]]
    assert len(missing) > 0


def test_no_jd_returns_none():
    result = match_keywords(RESUME_TEXT, None)
    assert result["score"] is None
    assert result["match_percentage"] is None
    assert result["message"] is not None


def test_empty_jd_returns_none():
    result = match_keywords(RESUME_TEXT, "")
    assert result["score"] is None


def test_match_percentage():
    result = match_keywords(RESUME_TEXT, JD_TEXT)
    assert result["total_keywords"] > 0
    assert 0 <= result["match_percentage"] <= 100
    assert result["score"] == result["match_percentage"]
