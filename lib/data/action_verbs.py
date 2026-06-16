ACTION_VERBS = {
    "leadership": [
        "led", "directed", "managed", "supervised", "oversaw", "coordinated",
        "orchestrated", "guided", "mentored", "coached", "spearheaded",
        "chaired", "commanded", "governed", "presided", "stewarded",
        "administered", "captained", "moderated", "facilitated",
    ],
    "achievement": [
        "achieved", "accomplished", "attained", "delivered", "earned",
        "exceeded", "outperformed", "realized", "secured", "surpassed",
        "won", "completed", "fulfilled", "reached", "succeeded",
    ],
    "creation": [
        "created", "designed", "developed", "built", "established",
        "founded", "launched", "pioneered", "architected", "crafted",
        "devised", "engineered", "forged", "formulated", "instituted",
        "introduced", "invented", "originated", "produced", "shaped",
    ],
    "improvement": [
        "improved", "enhanced", "optimized", "upgraded", "refined",
        "revamped", "overhauled", "restructured", "streamlined",
        "strengthened", "boosted", "elevated", "maximized", "modernized",
        "transformed", "accelerated", "advanced", "amplified", "augmented",
    ],
    "analysis": [
        "analyzed", "assessed", "evaluated", "researched", "investigated",
        "audited", "diagnosed", "examined", "explored", "inspected",
        "interpreted", "measured", "reviewed", "scrutinized", "surveyed",
        "tested", "validated", "verified", "appraised", "calculated",
    ],
    "communication": [
        "communicated", "presented", "authored", "documented",
        "negotiated", "persuaded", "reported", "articulated",
        "briefed", "conveyed", "drafted", "influenced", "liaised",
        "mediated", "pitched", "promoted", "publicized", "published",
    ],
    "collaboration": [
        "collaborated", "partnered", "teamed", "allied", "contributed",
        "cooperated", "united", "assisted", "supported", "aided",
        "consulted", "counseled", "participated", "volunteered",
    ],
    "execution": [
        "implemented", "executed", "deployed", "operated", "processed",
        "conducted", "carried", "performed", "integrated", "automated",
        "configured", "maintained", "monitored", "programmed",
        "provisioned", "resolved", "troubleshot", "troubleshooted",
    ],
    "growth": [
        "grew", "expanded", "increased", "scaled", "generated",
        "drove", "propelled", "catalyzed", "galvanized", "mobilized",
        "rallied", "spurred", "stimulated", "yielded",
    ],
    "strategy": [
        "strategized", "planned", "forecasted", "projected",
        "conceptualized", "envisioned", "ideated", "incubated",
        "initiated", "innovated", "mapped", "prioritized", "roadmapped",
    ],
    "reduction": [
        "reduced", "cut", "eliminated", "minimized", "decreased",
        "consolidated", "curtailed", "diminished", "lowered",
        "mitigated", "slashed", "trimmed",
    ],
    "technical": [
        "coded", "programmed", "debugged", "refactored", "migrated",
        "containerized", "virtualized", "compiled", "scripted",
        "backed", "restored", "replicated", "synchronized",
        "encrypted", "decrypted", "hashed", "tokenized",
        "indexed", "queried", "benchmarked",
    ],
    "saved": [
        "saved", "conserved", "preserved", "reclaimed", "recovered",
        "redeemed", "rescued", "salvaged", "spared",
    ],
    "taught": [
        "taught", "educated", "instructed", "trained", "onboarded",
        "lectured", "demonstrated", "illustrated", "explained",
        "simplified", "clarified", "demystified",
    ],
}

FLAT_ACTION_VERBS = sorted(set(
    verb for verbs in ACTION_VERBS.values() for verb in verbs
))

QUANTIFICATION_PATTERNS = [
    r"\$\s*\d[\d,.]*",            # dollar amounts: $50,000
    r"\d+\s*%",                    # percentages: 25%
    r"\d+[\d,.]*\s*(?:users|customers|clients|people|employees|staff|members|visitors|downloads|installs)",
    r"\d+[\d,.]*\s*(?:x|times|fold)",  # multipliers: 3x, 10 times
    r"\d+[\d,.]*\s*(?:hours|days|weeks|months|years|minutes|seconds)",
    r"\d+[\d,.]*\s*(?:dollars|usd|eur|gbp|inr)",  # currency words
    r"\d+[\d,.]*\s*(?:percent|pct)",  # percent words
    r"\b(?:increased|decreased|grew|reduced|saved|generated|delivered|managed|led|handled)\s+\S+\s+(?:by|from|to)\s+\d+",
]
