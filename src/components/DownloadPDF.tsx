"use client"

import { useState } from "react"
import { Download, Loader2 } from "lucide-react"
import { Button } from "@/components/ui/button"

interface Dimension {
  name: string
  key: string
  score: number
  max: number
}

interface Issue {
  severity: string
  message: string
}

interface Keyword {
  keyword: string
  type?: string
}

interface MissingSkill {
  skill: string
  mentions_in_jd: number
  priority: string
}

interface AnalysisResult {
  overall_score: number
  dimensions: Dimension[]
  ats: {
    score: number
    issues: Issue[]
    details: Record<string, unknown>
  }
  sections: {
    score: number
    issues: Issue[]
    found_sections: Record<string, unknown>
    missing_sections: string[]
    bonus_sections: string[]
  }
  verbs: {
    score: number
    verb_score: number
    quantification_score: number
    verb_count: number
    bullet_count: number
    quantified_bullet_count: number
    issues: Issue[]
    suggestions: string[]
    details: Record<string, unknown>
  }
  keywords: {
    score: number | null
    matched_keywords: Keyword[]
    missing_keywords: Keyword[]
    total_keywords: number
    matched_count: number
    missing_count: number
    match_percentage: number | null
    message?: string
  }
  skills: {
    score: number | null
    matched_skills: { skill: string; mentions_in_jd: number }[]
    missing_skills: MissingSkill[]
    total_required: number
    matched_count: number
    missing_count: number
    match_percentage: number | null
    suggestions: string[]
    message?: string
  }
  metadata: {
    filename: string
    text_length: number
    word_count: number
  }
}

function sColor(s: number): string {
  if (s >= 80) return "#10b981"
  if (s >= 60) return "#f59e0b"
  return "#ef4444"
}

function sevBg(severity: string): string {
  if (severity === "high") return "#fef2f2"
  if (severity === "medium") return "#fffbeb"
  return "#f3f4f6"
}

function sevTxt(severity: string): string {
  if (severity === "high") return "#dc2626"
  if (severity === "medium") return "#d97706"
  return "#6b7280"
}

function buildReportHTML(result: AnalysisResult): string {
  const { ats, sections, verbs, keywords, skills } = result

  const dimensionCards = result.dimensions.map((dim) =>
    `<div style="flex:1 1 90px;text-align:center;padding:8px 6px;background:#f9fafb;border-radius:4px;border:1px solid #e5e7eb">
      <p style="font-size:20px;font-weight:700;margin:0 0 2px;color:${sColor(dim.score)}">${dim.score}%</p>
      <p style="font-size:10px;color:#636363;margin:0">${dim.name}</p>
    </div>`
  ).join("")

  const atsIssues = ats.issues.length > 0
    ? ats.issues.map((i) =>
        `<div style="font-size:11px;margin-bottom:3px;display:flex;gap:5px;align-items:flex-start">
          <span style="padding:0 5px;border-radius:3px;font-size:9px;font-weight:600;text-transform:uppercase;background:${sevBg(i.severity)};color:${sevTxt(i.severity)};white-space:nowrap">${i.severity}</span>
          <span style="color:#4b5563">${i.message}</span>
        </div>`
      ).join("")
    : `<p style="font-size:11px;color:#10b981;margin:0">No ATS issues detected</p>`

  const foundSections = (Object.values(sections.found_sections) as Array<{ canonical_name?: string }>)
    .map((s) => `<span style="display:inline-block;padding:1px 6px;margin:1px;background:#ecfdf5;color:#059669;border-radius:3px;font-size:10px">${s?.canonical_name || ""}</span>`).join("")
  const missingSections = sections.missing_sections
    .map((s) => `<span style="display:inline-block;padding:1px 6px;margin:1px;background:#fef2f2;color:#dc2626;border-radius:3px;font-size:10px">${s}</span>`).join("")

  const verbsIssues = verbs.issues.map((i) =>
    `<div style="font-size:11px;margin-bottom:3px;display:flex;gap:5px;align-items:flex-start">
      <span style="padding:0 5px;border-radius:3px;font-size:9px;font-weight:600;text-transform:uppercase;background:${sevBg(i.severity)};color:${sevTxt(i.severity)};white-space:nowrap">${i.severity}</span>
      <span style="color:#4b5563">${i.message}</span>
    </div>`
  ).join("")

  const verbsSuggestions = verbs.suggestions.map((s) =>
    `<p style="font-size:11px;color:#3c68d9;margin:2px 0">${s}</p>`
  ).join("")

  let keywordsSection = ""
  if (keywords.match_percentage !== null) {
    const missingHTML = keywords.missing_keywords.length > 0
      ? `<div><p style="font-size:10px;font-weight:600;color:#dc2626;margin:4px 0 2px">Missing (${keywords.missing_keywords.length})</p>
         <div style="display:flex;flex-wrap:wrap;gap:3px">
           ${keywords.missing_keywords.slice(0, 30).map((k) =>
             `<span style="padding:1px 5px;background:#fef2f2;color:#dc2626;border-radius:3px;font-size:9px">${k.keyword}</span>`
           ).join("")}
         </div></div>`
      : ""

    keywordsSection = `
      <div style="margin-bottom:14px">
        <h2 style="font-size:14px;font-weight:700;margin:0 0 6px;border-bottom:1px solid #e5e7eb;padding-bottom:3px;color:#1a1a1a">
          <span style="color:${sColor(keywords.match_percentage)};margin-right:6px">${keywords.match_percentage}%</span>
          Keyword Match
        </h2>
        <p style="font-size:11px;color:#636363;margin:0 0 4px">${keywords.matched_count} of ${keywords.total_keywords} JD keywords matched</p>
        ${missingHTML}
      </div>`
  }

  let skillsSection = ""
  if (skills.match_percentage !== null) {
    const criticalMissing = skills.missing_skills.filter((s) => s.priority === "high")
    const criticalHTML = criticalMissing.length > 0
      ? `<div><p style="font-size:10px;font-weight:600;color:#dc2626;margin:4px 0 2px">Critical Gaps</p>
         <div style="display:flex;flex-wrap:wrap;gap:3px">
           ${criticalMissing.slice(0, 10).map((s) =>
             `<span style="padding:1px 5px;background:#fef2f2;color:#dc2626;border-radius:3px;font-size:9px">${s.skill}</span>`
           ).join("")}
         </div></div>`
      : ""

    skillsSection = `
      <div style="margin-bottom:14px">
        <h2 style="font-size:14px;font-weight:700;margin:0 0 6px;border-bottom:1px solid #e5e7eb;padding-bottom:3px;color:#1a1a1a">
          <span style="color:${sColor(skills.match_percentage)};margin-right:6px">${skills.match_percentage}%</span>
          Skill Match
        </h2>
        <p style="font-size:11px;color:#636363;margin:0 0 4px">${skills.matched_count} of ${skills.total_required} required skills matched</p>
        ${skills.suggestions.map((s) => `<p style="font-size:11px;color:#3c68d9;margin:2px 0">${s}</p>`).join("")}
        ${criticalHTML}
      </div>`
  }

  return `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>ResumeScanner Report</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: system-ui, -apple-system, sans-serif; padding: 40px; color: #1a1a1a; max-width: 700px; margin: 0 auto; }
    @page { margin: 0.5in; size: A4; }
  </style>
</head>
<body>
  <div style="text-align:center;margin-bottom:20px;border-bottom:2px solid #3c68d9;padding-bottom:12px">
    <h1 style="font-size:22px;font-weight:700;margin:0 0 4px">ResumeScanner Report</h1>
    <p style="font-size:12px;color:#636363;margin:0">
      ${result.metadata.filename} — ${result.metadata.word_count} words — ${new Date().toLocaleDateString()}
    </p>
  </div>

  <div style="text-align:center;margin-bottom:16px;padding:14px;background:#f3f4f6;border-radius:6px">
    <p style="font-size:12px;color:#636363;margin:0 0 3px;text-transform:uppercase;font-weight:600">Overall Score</p>
    <p style="font-size:44px;font-weight:800;margin:0;color:${sColor(result.overall_score)}">${result.overall_score}%</p>
  </div>

  <div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px">
    ${dimensionCards}
  </div>

  <div style="margin-bottom:14px">
    <h2 style="font-size:14px;font-weight:700;margin:0 0 6px;border-bottom:1px solid #e5e7eb;padding-bottom:3px;color:#1a1a1a">
      <span style="color:${sColor(ats.score)};margin-right:6px">${ats.score}%</span>
      ATS Compatibility
    </h2>
    ${atsIssues}
  </div>

  <div style="margin-bottom:14px">
    <h2 style="font-size:14px;font-weight:700;margin:0 0 6px;border-bottom:1px solid #e5e7eb;padding-bottom:3px;color:#1a1a1a">
      <span style="color:${sColor(sections.score)};margin-right:6px">${sections.score}%</span>
      Sections
    </h2>
    <div style="margin-bottom:4px">${foundSections} ${missingSections}</div>
    ${sections.issues.map((i) =>
      `<div style="font-size:11px;margin-bottom:3px;display:flex;gap:5px;align-items:flex-start">
        <span style="padding:0 5px;border-radius:3px;font-size:9px;font-weight:600;text-transform:uppercase;background:${sevBg(i.severity)};color:${sevTxt(i.severity)};white-space:nowrap">${i.severity}</span>
        <span style="color:#4b5563">${i.message}</span>
      </div>`
    ).join("")}
  </div>

  <div style="margin-bottom:14px">
    <h2 style="font-size:14px;font-weight:700;margin:0 0 6px;border-bottom:1px solid #e5e7eb;padding-bottom:3px;color:#1a1a1a">
      <span style="color:${sColor(verbs.score)};margin-right:6px">${verbs.score}%</span>
      Action Verbs &amp; Quantification
    </h2>
    <div style="display:flex;gap:10px;font-size:11px;margin-bottom:6px">
      <div style="flex:1;padding:6px;background:#f9fafb;border-radius:3px;text-align:center">
        <p style="font-weight:700;margin:0;font-size:15px;color:#1a1a1a">${verbs.verb_count}</p>
        <p style="color:#636363;margin:0;font-size:9px">Action Verbs</p>
      </div>
      <div style="flex:1;padding:6px;background:#f9fafb;border-radius:3px;text-align:center">
        <p style="font-weight:700;margin:0;font-size:15px;color:#1a1a1a">${verbs.quantified_bullet_count}/${verbs.bullet_count}</p>
        <p style="color:#636363;margin:0;font-size:9px">Quantified Bullets</p>
      </div>
    </div>
    ${verbsIssues}
    ${verbsSuggestions}
  </div>

  ${keywordsSection}
  ${skillsSection}

  <div style="border-top:1px solid #e5e7eb;padding-top:10px;text-align:center;font-size:9px;color:#9ca3af">
    <p style="margin:0">Generated by ResumeScanner — Free ATS Resume Analyzer — MIT License</p>
  </div>
</body>
</html>`
}

export function DownloadPDF({ result }: { result: AnalysisResult }) {
  const [loading, setLoading] = useState(false)

  function handleDownload() {
    setLoading(true)

    const html = buildReportHTML(result)
    const w = window.open("", "_blank")
    if (!w) {
      setLoading(false)
      return
    }
    w.document.write(html)
    w.document.close()
    w.focus()

    setTimeout(() => {
      w.print()
      setLoading(false)
    }, 500)
  }

  return (
    <Button onClick={handleDownload} disabled={loading} variant="outline" size="lg" className="gap-2">
      {loading ? (
        <>
          <Loader2 className="h-4 w-4 animate-spin" />
          Opening...
        </>
      ) : (
        <>
          <Download className="h-4 w-4" />
          Download Report (PDF)
        </>
      )}
    </Button>
  )
}
