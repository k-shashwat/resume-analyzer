"""TF-IDF word weights — maps common English words to low IDF scores so
generic filler words don't dilute keyword matching. Words NOT in this map
get a high default IDF, meaning they are considered domain-specific."""

# IDF = log(1,000,000 / estimated_corpus_frequency)
# Higher IDF → more specific/important
# Lower IDF → very common, generic

COMMON_WORD_IDF: dict[str, float] = {
    # Top 50 most common English words (function words) — near-zero IDF
    "the": 1.0, "a": 1.0, "an": 1.0, "and": 1.0, "or": 1.0, "but": 1.0,
    "in": 1.0, "on": 1.0, "at": 1.0, "to": 1.0, "for": 1.0, "of": 1.0,
    "with": 1.0, "by": 1.0, "from": 1.0, "as": 1.0, "is": 1.0, "was": 1.0,
    "are": 1.5, "were": 1.5, "be": 1.5, "been": 1.5, "being": 1.5,
    "have": 1.5, "has": 1.5, "had": 1.5, "do": 1.5, "does": 1.5,
    "did": 1.5, "will": 1.5, "would": 1.5, "could": 1.5, "should": 1.5,
    "may": 1.5, "might": 1.5, "can": 1.5, "shall": 1.5,
    "you": 1.5, "your": 1.5, "we": 1.5, "our": 1.5, "they": 1.5,
    "their": 1.5, "it": 1.5, "its": 1.5, "this": 2.0, "that": 2.0,
    "these": 2.5, "those": 2.5,

    # Very common verbs — low IDF
    "make": 2.0, "use": 1.5, "need": 2.0, "take": 2.0, "get": 2.0,
    "give": 2.5, "find": 2.5, "help": 2.0, "work": 1.5, "set": 2.0,
    "put": 2.5, "run": 2.5, "build": 2.0, "create": 2.0, "develop": 2.0,
    "design": 2.0, "implement": 2.5, "manage": 2.5, "lead": 2.5,
    "support": 2.5, "provide": 2.5, "drive": 2.5, "deliver": 2.5,
    "ensure": 2.5, "improve": 2.5, "increase": 2.5, "reduce": 2.5,
    "maintain": 2.5, "identify": 2.5, "define": 2.5, "establish": 3.0,
    "allow": 2.5, "enable": 2.5, "require": 2.5, "include": 2.5,
    "understand": 3.0, "learn": 3.0, "teach": 3.5, "train": 3.0,
    "apply": 3.0, "approach": 3.0, "articulate": 5.0,

    # Very common nouns — low IDF
    "time": 2.0, "year": 2.0, "day": 2.5, "month": 3.0,
    "people": 2.0, "person": 2.5, "man": 2.5, "woman": 3.0,
    "work": 1.5, "job": 2.5, "role": 2.5, "position": 2.5,
    "team": 2.0, "company": 2.5, "business": 1.5, "client": 3.0,
    "customer": 3.0, "user": 3.0, "partner": 3.0, "stakeholder": 4.0,
    "service": 2.5, "product": 2.5, "solution": 2.5,
    "experience": 1.5, "skill": 2.0, "knowledge": 2.5,
    "opportunity": 3.0, "growth": 3.0, "impact": 3.0,
    "data": 2.0, "information": 3.0, "insight": 3.5,
    "result": 3.0, "process": 2.5, "system": 2.5,
    "project": 2.5, "program": 3.0, "initiative": 4.0,
    "industry": 3.0, "market": 3.0, "field": 3.5,
    "background": 3.5, "education": 3.5, "degree": 3.5,
    "requirement": 3.5, "qualification": 4.5,
    "application": 3.0, "technology": 3.0, "platform": 3.5,
    "environment": 3.5, "culture": 4.0, "value": 3.5,
    "benefit": 3.5, "compensation": 4.5, "salary": 4.5,

    # Very common adjectives — low IDF
    "good": 2.0, "great": 2.5, "best": 2.5, "better": 2.5,
    "new": 2.0, "old": 3.0, "high": 2.0, "low": 2.5,
    "large": 2.5, "small": 2.5, "big": 2.5,
    "strong": 2.5, "key": 2.5, "critical": 3.5,
    "important": 3.0, "relevant": 3.5, "essential": 4.0,
    "different": 3.0, "same": 3.0, "similar": 3.5,
    "able": 2.5, "available": 3.0, "potential": 3.5,
    "current": 3.0, "previous": 3.5, "future": 3.5,
    "complete": 3.5, "entire": 4.0, "full": 3.0,
    "real": 3.0, "actual": 3.5, "specific": 3.5,
    "additional": 3.5, "multiple": 3.5, "various": 3.5,
    "major": 3.5, "significant": 4.0, "successful": 4.0,
    "positive": 4.0, "negative": 4.0, "effective": 4.0,
    "advanced": 4.0, "basic": 4.0, "complex": 4.0,
    "easy": 3.5, "difficult": 4.0, "simple": 3.5,
    "fast": 3.5, "quick": 3.5, "slow": 4.0,
    "long": 3.0, "short": 3.5, "deep": 3.5,
    "wide": 3.5, "broad": 4.0, "narrow": 4.5,
    "clear": 3.5, "open": 3.0, "close": 3.5,
    "right": 3.0, "wrong": 4.0, "true": 3.5,
    "possible": 3.5, "likely": 4.0, "necessary": 4.0,
    "common": 3.5, "standard": 3.5, "typical": 4.0,
    "professional": 4.0, "personal": 3.5, "technical": 3.5,
    "excellent": 4.0, "outstanding": 5.0, "proven": 4.5,
    "exceptional": 5.0, "superior": 5.0, "unique": 4.5,
    "proactive": 5.0, "innovative": 4.5, "creative": 4.0,
    "strategic": 4.0, "operational": 4.5, "tactical": 5.0,
    "detail": 3.5, "quality": 3.0, "excellence": 4.5,

    # More common JD words that aren't domain-specific
    "collaboration": 4.0, "communication": 3.5, "presentation": 4.5,
    "leadership": 4.0, "management": 3.0, "mentoring": 5.0,
    "coaching": 5.0, "training": 3.0, "development": 2.5,
    "planning": 3.5, "execution": 4.0, "strategy": 3.5,
    "analysis": 3.5, "research": 3.5, "reporting": 4.0,
    "writing": 4.0, "documentation": 4.5, "testing": 3.5,
    "integration": 4.0, "deployment": 4.0, "operation": 3.5,
    "optimization": 4.5, "automation": 4.5, "scalability": 5.0,
    "performance": 3.5, "security": 3.5, "compliance": 4.5,
    "governance": 5.0, "risk": 4.0, "monitoring": 4.5,
    "evaluation": 4.5, "assessment": 4.5, "measurement": 5.0,
    "science": 3.5, "engineering": 3.5, "mathematics": 5.0,
    "physics": 5.5, "chemistry": 5.5, "biology": 5.0,
    "design": 2.0, "architecture": 4.0, "framework": 4.0,
    "methodology": 4.5, "approach": 3.0, "technique": 4.0,
    "tool": 3.5, "resource": 3.5, "capability": 4.0,
    "functionality": 4.5, "feature": 4.0, "component": 4.5,
    "module": 4.5, "interface": 4.5, "database": 4.5,
    "network": 4.0, "server": 4.0, "storage": 4.5,
    "infrastructure": 4.5, "hardware": 4.5, "software": 4.0,
    "content": 3.5, "channel": 3.5, "campaign": 4.0,
    "conversion": 4.5, "revenue": 4.5, "profit": 4.5,
    "cost": 4.0, "budget": 4.5, "investment": 4.5,
    "pipeline": 4.5, "workflow": 4.5, "roadmap": 5.0,
    "forecast": 5.0, "predict": 5.0, "model": 3.5,
    "algorithm": 5.0, "method": 4.0, "procedure": 5.0,
    "policy": 4.5, "rule": 4.0, "regulation": 5.0,
    "standard": 3.5, "protocol": 5.0, "pattern": 4.5,

    # Words that are common BUT in JD context are noise
    "etc": 1.5, "plus": 2.5, "across": 2.5, "among": 2.5,
    "within": 2.5, "without": 2.5, "along": 2.5, "between": 2.5,
    "during": 2.5, "through": 2.5, "around": 3.0, "about": 2.0,
    "every": 2.5, "each": 2.5, "any": 2.5, "all": 2.0,
    "some": 2.5, "many": 2.5, "much": 3.0, "few": 3.0,
    "other": 2.5, "another": 3.0, "own": 3.0, "such": 2.5,
    "just": 2.5, "only": 2.5, "also": 2.0, "well": 2.5,
    "even": 2.5, "still": 3.0, "yet": 3.0, "already": 3.5,
    "always": 3.0, "never": 3.5, "often": 3.5, "usually": 4.0,
    "today": 3.0, "now": 3.0, "then": 3.0,
    "here": 3.0, "there": 3.0, "where": 3.0,
    "however": 3.5, "therefore": 4.5, "thus": 4.5,
    "although": 4.0, "because": 3.5, "since": 3.0,
    "while": 3.0, "when": 3.0, "before": 3.0, "after": 3.0,
    "first": 3.0, "last": 3.0, "next": 3.0, "previous": 3.5,
    "following": 3.5, "above": 3.5, "below": 3.5,
    "example": 3.5, "way": 3.0, "part": 3.0, "kind": 3.5,
    "type": 3.5, "form": 3.5, "level": 3.5, "rate": 4.0,
    "number": 3.5, "amount": 4.0, "size": 4.0, "scope": 4.5,
    "range": 4.0, "scale": 4.0, "extent": 4.5, "degree": 4.0,
    "point": 3.5, "case": 3.5, "issue": 3.5, "problem": 3.5,
    "challenge": 4.0, "goal": 4.0, "objective": 4.5, "target": 4.0,
    "outcome": 4.5, "output": 4.5, "input": 4.5,
    "step": 3.5, "phase": 4.0, "stage": 4.0, "iteration": 5.0,
    "change": 3.5, "improvement": 4.0, "enhancement": 5.0,
    "update": 4.0, "upgrade": 4.5, "modification": 5.0,
    "task": 4.0, "activity": 4.0, "action": 4.0,
    "item": 4.0, "element": 4.5, "aspect": 4.5,
    "area": 3.5, "domain": 4.5, "sector": 4.5,
    "region": 4.5, "location": 4.0, "place": 3.5,
    "country": 4.0, "world": 3.5, "global": 4.0,
    "local": 3.5, "national": 4.5, "international": 5.0,
}

DEFAULT_IDF = 12.0   # log(1,000,000 / 6) — for rare/domain-specific terms
MAX_IDF = 14.0


def get_word_idf(word: str) -> float:
    """Return the IDF score for a single word. Higher = more specific."""
    return COMMON_WORD_IDF.get(word.lower(), DEFAULT_IDF)


def term_specificity_score(term: str) -> float:
    """Score how specific/domain-relevant a term is.
    Multi-word terms are weighted higher; rare words get higher IDF."""
    words = term.lower().split()
    if not words:
        return 0.0
    avg_idf = sum(get_word_idf(w) for w in words) / len(words)
    phrase_bonus = min(1.5, 1.0 + (len(words) - 1) * 0.25)
    return avg_idf * phrase_bonus
