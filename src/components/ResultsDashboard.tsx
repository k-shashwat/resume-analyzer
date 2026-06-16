"use client"

import { useMemo } from "react"
import { RefreshCw, Award, Zap, FileCheck, Search, Brain } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Card, CardContent } from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"
import { ScoreRadar } from "@/components/ScoreRadar"
import { DimensionCard } from "@/components/DimensionCard"
import { cn } from "@/lib/utils"

interface Dimension {
  name: string
  key: string
  score: number
  max: number
}

interface AnalysisResult {
  overall_score: number
  dimensions: Dimension[]
  ats: { score: number; issues: { severity: string; message: string }[]; details: Record<string, unknown> }
  sections: { score: number; issues: { severity: string; message: string; section?: string }[]; found_sections: Record<string, unknown>; missing_sections: string[]; bonus_sections: string[] }
  verbs: {
    score: number
    verb_score: number
    quantification_score: number
    found_action_verbs: string[]
    verb_count: number
    bullet_count: number
    quantified_bullet_count: number
    issues: { severity: string; message: string }[]
    suggestions: string[]
    details: Record<string, unknown>
  }
  keywords: {
    score: number | null
    matched_keywords: { keyword: string; type: string }[]
    missing_keywords: { keyword: string; type: string }[]
    total_keywords: number
    matched_count: number
    missing_count: number
    match_percentage: number | null
    message?: string
  }
  skills: {
    score: number | null
    matched_skills: { skill: string; mentions_in_jd: number }[]
    missing_skills: { skill: string; mentions_in_jd: number; priority: string }[]
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

interface ResultsDashboardProps {
  result: AnalysisResult
  onReset: () => void
}

function scoreColor(score: number): string {
  if (score >= 80) return "text-emerald-500"
  if (score >= 60) return "text-amber-500"
  return "text-red-500"
}

function scoreBg(score: number): string {
  if (score >= 80) return "bg-emerald-500/10"
  if (score >= 60) return "bg-amber-500/10"
  return "bg-red-500/10"
}

const dimensionIcons: Record<string, typeof Award> = {
  ats: FileCheck,
  sections: Zap,
  verbs: Award,
  keywords: Search,
  skills: Brain,
}

export function ResultsDashboard({ result, onReset }: ResultsDashboardProps) {
  const dimensionCards = useMemo(() => {
    return result.dimensions.map((dim) => {
      const Icon = dimensionIcons[dim.key] || Award
      return (
        <Card key={dim.key} className="flex-1 min-w-[140px]">
          <CardContent className="p-4 text-center">
            <Icon className="h-5 w-5 mx-auto mb-2 text-muted-foreground" />
            <p className={cn("text-2xl font-bold", scoreColor(dim.score))}>
              {dim.score}%
            </p>
            <p className="text-xs text-muted-foreground mt-1">{dim.name}</p>
          </CardContent>
        </Card>
      )
    })
  }, [result.dimensions])

  return (
    <div className="w-full max-w-5xl mx-auto space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
      <div className="text-center">
        <Badge variant="outline" className="mb-3 text-xs">
          {result.metadata.filename}
        </Badge>
        <div className={cn("inline-flex items-center gap-4 px-8 py-4 rounded-2xl", scoreBg(result.overall_score))}>
          <div>
            <p className="text-sm font-medium text-muted-foreground">Overall Score</p>
            <p className={cn("text-5xl font-bold tracking-tight", scoreColor(result.overall_score))}>
              {result.overall_score}
            </p>
          </div>
          <Separator orientation="vertical" className="h-12" />
          <div className="text-left">
            <p className="text-sm font-medium text-muted-foreground">ResumeScanner</p>
            <p className="text-xs text-muted-foreground">
              {result.metadata.word_count} words analyzed
            </p>
          </div>
        </div>
      </div>

      <div className="flex flex-wrap gap-3 justify-center">
        {dimensionCards}
      </div>

      <div className="grid lg:grid-cols-2 gap-8">
        <div className="flex items-center justify-center">
          <ScoreRadar dimensions={result.dimensions} />
        </div>
        <div className="space-y-4">
          <DimensionCard
            title="ATS Compatibility"
            score={result.ats.score}
            issues={result.ats.issues}
            details={result.ats.details}
          />
          <DimensionCard
            title="Sections"
            score={result.sections.score}
            issues={result.sections.issues}
            details={{
              "Found": Object.keys(result.sections.found_sections).length,
              "Missing": result.sections.missing_sections.join(", ") || "None",
              "Bonus": result.sections.bonus_sections.join(", ") || "None",
            }}
          />
        </div>
      </div>

      <div className="grid md:grid-cols-2 gap-6">
        <DimensionCard
          title="Action Verbs & Quantification"
          score={result.verbs.score}
          issues={result.verbs.issues}
          suggestions={result.verbs.suggestions}
          details={{
            "Action Verbs": result.verbs.verb_count,
            "Bullet Points": result.verbs.bullet_count,
            "Quantified": result.verbs.quantified_bullet_count,
            "Verb Density": `${result.verbs.details.verb_density}/1k words`,
            "Quant Rate": `${result.verbs.details.quantification_rate}%`,
          }}
        />
        <DimensionCard
          title="Keyword Match"
          score={result.keywords.score}
          issues={result.keywords.message ? [{ severity: "low", message: result.keywords.message }] : []}
          matched={result.keywords.matched_keywords}
          missing={result.keywords.missing_keywords}
          details={{
            "Matched": result.keywords.matched_count,
            "Missing": result.keywords.missing_count,
            "Total JD Keywords": result.keywords.total_keywords,
          }}
        />
      </div>

      <DimensionCard
        title="Skill Gap Analysis"
        score={result.skills.score}
        issues={result.skills.missing_skills
          .filter((s) => s.priority === "high")
          .slice(0, 5)
          .map((s) => ({
            severity: "high" as const,
            message: `Missing critical skill: ${s.skill} (${s.mentions_in_jd}x in JD)`,
          }))}
        suggestions={result.skills.suggestions}
        matched={result.skills.matched_skills.map((s) => ({ keyword: s.skill }))}
        missing={result.skills.missing_skills.map((s) => ({ keyword: s.skill }))}
        details={{
          "Skills Matched": result.skills.matched_count,
          "Skills Missing": result.skills.missing_count,
          "Total Required": result.skills.total_required,
        }}
      />

      <div className="flex justify-center pt-4">
        <Button onClick={onReset} variant="outline" size="lg" className="gap-2">
          <RefreshCw className="h-4 w-4" />
          Analyze Another Resume
        </Button>
      </div>
    </div>
  )
}
