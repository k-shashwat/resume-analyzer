"use client"

import {
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  Radar,
  ResponsiveContainer,
  PolarRadiusAxis,
} from "recharts"
import { cn } from "@/lib/utils"

interface Dimension {
  name: string
  key: string
  score: number
  max: number
}

interface ScoreRadarProps {
  dimensions: Dimension[]
  className?: string
}

export function ScoreRadar({ dimensions, className }: ScoreRadarProps) {
  const data = dimensions.map((d) => ({
    dimension: d.name,
    score: d.score,
    max: d.max,
  }))

  if (data.length === 0) return null

  return (
    <div className={cn("w-full aspect-square max-w-[300px] mx-auto", className)}>
      <ResponsiveContainer width="100%" height="100%">
        <RadarChart data={data} cx="50%" cy="50%" outerRadius="75%">
          <PolarGrid stroke="var(--border)" />
          <PolarAngleAxis
            dataKey="dimension"
            tick={{ fill: "var(--muted-foreground)", fontSize: 11 }}
          />
          <PolarRadiusAxis
            angle={90}
            domain={[0, 100]}
            tick={{ fill: "var(--muted-foreground)", fontSize: 10 }}
            axisLine={false}
          />
          <Radar
            name="Score"
            dataKey="score"
            fill="var(--primary)"
            fillOpacity={0.3}
            stroke="var(--primary)"
            strokeWidth={2}
          />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  )
}
