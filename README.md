# ResumeScanner

Free, open-source ATS resume analyzer. Upload your resume, paste a job description, and get instant feedback on ATS compatibility, keyword matching, section structure, action verbs, quantification, and skill gaps — no sign-up required.

## Features

- **ATS Compatibility Score** — Detects images, tables, multi-column layouts, missing contact info, and other ATS pitfalls
- **Keyword Matching** — Lemmatization-based matching against the job description with multi-word phrase support
- **Section Analysis** — Detects expected resume sections with fuzzy matching (typo-tolerant)
- **Action Verb Scoring** — Checks for strong action verbs across ~200 curated verbs
- **Quantification Detection** — Identifies measurable achievements (dollar amounts, percentages, metrics)
- **Skill Gap Analysis** — Matches 1,000+ curated skills from the JD against your resume
- **Dark/Light Theme** — Built-in theme toggle with blue/green accents
- **Multi-dimensional Results** — Radar chart + dimension cards with per-issue suggestions

## Tech Stack

- **Frontend:** Next.js (App Router), TypeScript, Tailwind CSS, shadcn/ui, recharts
- **Backend:** FastAPI (Vercel Python serverless), pdfplumber, python-docx, spaCy
- **Hosting:** Vercel (free tier)

## Getting Started

### Prerequisites

- Node.js 20+
- Python 3.9+
- npm

### Setup

```bash
# Install Node dependencies
npm install

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

### Development

```bash
# Start the development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Running Tests

```bash
source venv/bin/activate
pytest tests/ -v
```

## Project Structure

```
resume-analyzer/
├── src/
│   ├── app/
│   │   ├── page.tsx              # Main upload + results page
│   │   ├── layout.tsx            # Root layout with theme provider
│   │   └── globals.css           # Custom blue/green theme
│   ├── components/
│   │   ├── UploadZone.tsx        # File upload + JD textarea
│   │   ├── ResultsDashboard.tsx  # Full results display
│   │   ├── ScoreRadar.tsx        # Radar chart (recharts)
│   │   ├── DimensionCard.tsx     # Individual dimension card
│   │   ├── ThemeProvider.tsx     # Dark/light theme wrapper
│   │   └── ThemeToggle.tsx       # Theme toggle button
│   └── components/ui/            # shadcn/ui components
├── api/
│   └── analyze.py                # FastAPI endpoint
├── lib/
│   ├── parser.py                 # PDF/DOCX parsing
│   ├── analyzer/
│   │   ├── ats.py                # ATS compatibility scoring
│   │   ├── keywords.py           # Keyword matching
│   │   ├── sections.py           # Section analysis
│   │   ├── verbs.py              # Action verb + quantification
│   │   └── skills.py             # Skill gap identification
│   └── data/
│       ├── action_verbs.py       # ~200 curated action verbs
│       ├── skills_ontology.py    # 1,000+ skills across domains
│       └── section_headers.py    # Section header mappings
├── tests/                        # pytest unit tests
├── vercel.json                   # Vercel deployment config
└── requirements.txt              # Python dependencies
```

## API

### `POST /api/analyze`

Upload a resume file (PDF or DOCX, max 5MB) with an optional job description.

**Request:** `multipart/form-data`
- `file` (required) — PDF or DOCX file
- `job_description` (optional) — Plain text job description (max 5,000 chars)

**Response:** JSON with overall score, dimension scores, and detailed analysis.

## Deployment

Push to GitHub and connect to Vercel. Vercel auto-detects Next.js and the Python runtime. Set `PYTHON_VERSION` env var if needed.

## License

MIT — see [LICENSE](LICENSE)
