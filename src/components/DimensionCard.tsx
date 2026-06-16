"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { cn } from "@/lib/utils"

interface Issue {
  severity: string
  message: string
  section?: string
  skill?: string
}

interface DimensionCardProps {
  title: string
  score: number | null
  issues: Issue[]
  suggestions?: string[]
  details?: Record<string, unknown>
  matched?: { keyword: string; type?: string }[]
  missing?: { keyword: string; type?: string }[]
  className?: string
}

function scoreColor(score: number): string {
  if (score >= 80) return "text-emerald-500"
  if (score >= 60) return "text-amber-500"
  return "text-red-500"
}

function severityVariant(severity: string): "destructive" | "default" | "secondary" {
  if (severity === "high") return "destructive"
  if (severity === "medium") return "default"
  return "secondary"
}

export function DimensionCard({
  title,
  score,
  issues,
  suggestions,
  details,
  matched,
  missing,
  className,
}: DimensionCardProps) {
  return (
    <Card className={cn("w-full", className)}>
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <CardTitle className="text-lg">{title}</CardTitle>
          {score !== null && score !== undefined ? (
            <span className={cn("text-2xl font-bold", scoreColor(score))}>
              {score}%
            </span>
          ) : (
            <span className="text-sm text-muted-foreground">N/A</span>
          )}
        </div>
        {score !== null && score !== undefined && (
          <Progress value={score} className="h-2" />
        )}
      </CardHeader>
      <CardContent className="space-y-4">
        {issues.length > 0 && (
          <div className="space-y-2">
            {issues.map((issue, i) => (
              <div key={i} className="flex items-start gap-2 text-sm">
                <Badge variant={severityVariant(issue.severity)} className="mt-0.5 shrink-0">
                  {issue.severity}
                </Badge>
                <span className="text-muted-foreground">{issue.message}</span>
              </div>
            ))}
          </div>
        )}

        {suggestions && suggestions.length > 0 && (
          <div className="space-y-1">
            <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wide">
              Suggestions
            </p>
            {suggestions.map((s, i) => (
              <p key={i} className="text-sm text-primary leading-relaxed">
                {s}
              </p>
            ))}
          </div>
        )}

        {matched && matched.length > 0 && (
          <div>
            <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wide mb-2">
              Matched ({matched.length})
            </p>
            <div className="flex flex-wrap gap-1.5">
              {matched.map((m, i) => (
                <Badge key={i} variant="outline" className="text-emerald-500 border-emerald-500/30">
                  {m.keyword}
                </Badge>
              ))}
            </div>
          </div>
        )}

        {missing && missing.length > 0 && (
          <div>
            <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wide mb-2">
              Missing ({missing.length})
            </p>
            <div className="flex flex-wrap gap-1.5">
              {missing.slice(0, 20).map((m, i) => (
                <Badge key={i} variant="outline" className="text-red-500 border-red-500/30">
                  {m.keyword}
                </Badge>
              ))}
              {missing.length > 20 && (
                <Badge variant="outline">+{missing.length - 20} more</Badge>
              )}
            </div>
          </div>
        )}

        {details && Object.keys(details).length > 0 && (
          <div className="grid grid-cols-2 gap-2 text-xs text-muted-foreground">
            {Object.entries(details).map(([key, value]) => (
              <div key={key} className="flex justify-between bg-muted rounded px-2 py-1">
                <span className="capitalize">{key.replace(/_/g, " ")}</span>
                <span className="font-mono">{String(value)}</span>
              </div>
            ))}
          </div>
        )}
      </CardContent>
    </Card>
  )
}
