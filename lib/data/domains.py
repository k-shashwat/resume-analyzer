"""Domain registry — maps 22 professional domains to acronym groups and skills categories."""

from typing import List, Dict, Set, Optional

# =============================================================================
# Domain definitions
# =============================================================================

DOMAINS: Dict[str, Dict] = {
    "all": {"label": "Auto-detect (all domains)", "icon": "🌐"},
    "tech": {"label": "Technology & Software", "icon": "💻"},
    "cloud": {"label": "Cloud & Infrastructure", "icon": "☁️"},
    "data": {"label": "Data & Analytics", "icon": "📊"},
    "finance": {"label": "Banking & Finance", "icon": "🏦"},
    "insurance": {"label": "Insurance", "icon": "🛡️"},
    "marketing": {"label": "Marketing & Sales", "icon": "📢"},
    "healthcare": {"label": "Healthcare & Pharma", "icon": "🏥"},
    "engineering": {"label": "Engineering & Manufacturing", "icon": "⚙️"},
    "automotive": {"label": "Automotive", "icon": "🚗"},
    "operations": {"label": "Operations & Supply Chain", "icon": "📦"},
    "legal": {"label": "Legal & Regulatory", "icon": "⚖️"},
    "hr": {"label": "HR & Recruitment", "icon": "👥"},
    "creative": {"label": "Creative & Design", "icon": "🎨"},
    "education": {"label": "Education & Research", "icon": "🎓"},
    "government": {"label": "Government & Public Sector", "icon": "🏛️"},
    "realestate": {"label": "Real Estate & Construction", "icon": "🏗️"},
    "energy": {"label": "Energy & Utilities", "icon": "⚡"},
    "retail": {"label": "Retail & E-Commerce", "icon": "🛒"},
    "media": {"label": "Media & Entertainment", "icon": "🎬"},
    "hospitality": {"label": "Hospitality & Tourism", "icon": "🏨"},
    "agriculture": {"label": "Agriculture & Food", "icon": "🌾"},
    "aviation": {"label": "Aviation & Aerospace", "icon": "✈️"},
}

DOMAIN_KEYS = list(DOMAINS.keys())
DOMAIN_LABELS = [{"key": k, "label": d["label"]} for k, d in DOMAINS.items()]


def get_domain_label(key: str) -> str:
    return DOMAINS.get(key, {}).get("label", key)


# =============================================================================
# Domain → Skills Ontology category mapping
# =============================================================================

DOMAIN_TO_SKILLS_CATEGORIES: Dict[str, Set[str]] = {
    "all": set(),  # all categories
    "tech": {"programming_languages", "frontend", "backend", "testing_qa",
             "mobile", "blockchain_web3", "embedded_hardware"},
    "cloud": {"devops_cloud", "security"},
    "data": {"databases", "ai_ml_data"},
    "finance": {"finance_banking", "programming_languages"},
    "insurance": {"finance_banking"},
    "marketing": {"sales_marketing", "design_creative", "product_project"},
    "healthcare": {"healthcare_life_sciences", "ai_ml_data"},
    "engineering": {"manufacturing_engineering", "embedded_hardware", "supply_chain"},
    "automotive": {"automotive", "manufacturing_engineering", "embedded_hardware"},
    "operations": {"supply_chain", "manufacturing_engineering"},
    "legal": {"legal_compliance", "security"},
    "hr": {"soft_skills", "product_project"},
    "creative": {"design_creative"},
    "education": {"soft_skills"},
    "government": {"legal_compliance", "security"},
    "realestate": {"supply_chain"},
    "energy": {"manufacturing_engineering", "supply_chain"},
    "retail": {"sales_marketing", "supply_chain"},
    "media": {"design_creative", "sales_marketing"},
    "hospitality": {"sales_marketing"},
    "agriculture": {"supply_chain"},
    "aviation": {"automotive", "manufacturing_engineering", "supply_chain"},
}

_cross_domain_categories = {"soft_skills", "certifications", "product_project", "other"}


def get_skills_categories_for_domain(domain: Optional[str]) -> Optional[Set[str]]:
    if not domain or domain == "all":
        return None
    cats = set(DOMAIN_TO_SKILLS_CATEGORIES.get(domain, set()))
    cats |= _cross_domain_categories
    return cats


# =============================================================================
# Domain → Acronym section mapping
# Maps domain keys to the comment section headers in acronyms.py
# =============================================================================

_ACRONYM_SECTION_MARKERS: Dict[str, str] = {
    "tech": "TECHNOLOGY & SOFTWARE",
    "cloud": "CLOUD & INFRASTRUCTURE",
    "data": "DATA & ANALYTICS",
    "finance": "BANKING & FINANCE",
    "insurance": "INSURANCE",
    "marketing": "MARKETING & SALES",
    "healthcare": "HEALTHCARE & PHARMA",
    "engineering": "ENGINEERING & MANUFACTURING",
    "automotive": "AUTOMOTIVE",
    "operations": "OPERATIONS & SUPPLY CHAIN",
    "legal": "LEGAL & REGULATORY",
    "hr": "HR & RECRUITMENT",
    "creative": "CREATIVE & DESIGN",
    "education": "EDUCATION & RESEARCH",
    "government": "GOVERNMENT & PUBLIC SECTOR",
    "realestate": "REAL ESTATE & CONSTRUCTION",
    "energy": "ENERGY & UTILITIES",
    "retail": "RETAIL & E-COMMERCE",
    "media": "MEDIA & ENTERTAINMENT",
    "hospitality": "HOSPITALITY & TOURISM",
    "agriculture": "AGRICULTURE & FOOD",
    "aviation": "AVIATION & AEROSPACE",
}

_cross_domain_sections = {"CROSS-DOMAIN", "GENERAL BUSINESS"}
_parsed_section_ranges: Optional[Dict[str, tuple[int, int]]] = None


def _parse_acronym_sections() -> Dict[str, tuple[int, int]]:
    """Parse acronyms.py to find line ranges for each domain section."""
    import os
    acronyms_path = os.path.join(os.path.dirname(__file__), "acronyms.py")
    ranges: Dict[str, tuple[int, int]] = {}
    with open(acronyms_path) as f:
        lines = f.readlines()
    current_start: Optional[int] = None
    current_domain: Optional[str] = None
    for i, line in enumerate(lines):
        if "====" in line:
            if current_start is not None and current_domain:
                ranges[current_domain] = (current_start, i - 2)
            current_start = i + 1
            current_domain = None
            for domain_key, marker in _ACRONYM_SECTION_MARKERS.items():
                if marker in line:
                    current_domain = domain_key
                    break
            if current_domain is None:
                for marker in _cross_domain_sections:
                    if marker in line:
                        current_domain = "cross"
                        break
    if current_start is not None and current_domain:
        ranges[current_domain] = (current_start, len(lines) - 1)
    return ranges


def get_acronym_group_indices_for_domain(domain: Optional[str]) -> Optional[set[int]]:
    """Return indices of acronym groups that belong to the given domain."""
    global _parsed_section_ranges
    if domain is None or domain == "all":
        return None
    if _parsed_section_ranges is None:
        _parsed_section_ranges = _parse_acronym_sections()
    from lib.data.acronyms import ACRONYM_GROUPS
    indices: set[int] = set()
    cross = _parsed_section_ranges.get("cross", (0, 0))
    for i in range(cross[0], cross[1] + 1):
        indices.add(i)
    domain_range = _parsed_section_ranges.get(domain)
    if domain_range:
        for i in range(domain_range[0], domain_range[1] + 1):
            indices.add(i)
    return indices
