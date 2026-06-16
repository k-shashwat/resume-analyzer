"use client"

import { useState } from "react"
import { FileSearch, Sparkles } from "lucide-react"
import { ThemeToggle } from "@/components/ThemeToggle"
import { UploadZone } from "@/components/UploadZone"
import { ResultsDashboard } from "@/components/ResultsDashboard"

export default function Home() {
  const [result, setResult] = useState<unknown>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [progress, setProgress] = useState("")

  async function handleAnalyze(file: File, jobDescription: string) {
    setLoading(true)
    setError(null)
    setResult(null)

    setProgress("Parsing resume...")

    const formData = new FormData()
    formData.append("file", file)
    if (jobDescription.trim()) {
      formData.append("job_description", jobDescription.trim())
    }

    try {
      setProgress("Analyzing keywords...")
      const res = await fetch("/api/analyze", {
        method: "POST",
        body: formData,
      })

      setProgress("Scoring sections...")

      const data = await res.json()

      if (!res.ok || data.error) {
        setError(data.error || "An unexpected error occurred. Please try again.")
        setResult(null)
      } else {
        setResult(data)
      }
    } catch {
      setError("Failed to connect to the server. Please check your connection and try again.")
    } finally {
      setLoading(false)
      setProgress("")
    }
  }

  function handleReset() {
    setResult(null)
    setError(null)
  }

  if (result) {
    return (
      <div className="flex-1 flex flex-col min-h-screen">
        <header className="sticky top-0 z-50 border-b bg-background/80 backdrop-blur-sm">
          <div className="max-w-5xl mx-auto flex items-center justify-between px-6 h-14">
            <div className="flex items-center gap-2">
              <FileSearch className="h-5 w-5 text-primary" />
              <span className="font-bold text-lg">ResumeScanner</span>
            </div>
            <ThemeToggle />
          </div>
        </header>
        <main className="flex-1 px-6 py-8 pb-16">
          <ResultsDashboard result={result as Parameters<typeof ResultsDashboard>[0]["result"]} onReset={handleReset} />
        </main>
      </div>
    )
  }

  return (
    <div className="flex-1 flex flex-col min-h-screen">
      <header className="sticky top-0 z-50 border-b bg-background/80 backdrop-blur-sm">
        <div className="max-w-5xl mx-auto flex items-center justify-between px-6 h-14">
          <div className="flex items-center gap-2">
            <FileSearch className="h-5 w-5 text-primary" />
            <span className="font-bold text-lg">ResumeScanner</span>
          </div>
          <ThemeToggle />
        </div>
      </header>

      <main className="flex-1 flex flex-col items-center justify-center px-6 py-16">
        <div className="text-center mb-12 space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 text-primary text-sm font-medium mb-2">
            <Sparkles className="h-3.5 w-3.5" />
            Free & Open Source
          </div>
          <h1 className="text-4xl font-bold tracking-tight">
            Optimize Your Resume for ATS
          </h1>
          <p className="text-lg text-muted-foreground max-w-lg mx-auto">
            Upload your resume and paste a job description. Get instant feedback on ATS compatibility, keywords, action verbs, and skill gaps — no sign-up required.
          </p>
        </div>

        <UploadZone onAnalyze={handleAnalyze} loading={loading} error={error} />

        {progress && (
          <div className="mt-8 text-center">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-primary/5 text-sm text-muted-foreground">
              <span className="animate-spin h-3.5 w-3.5 border-2 border-primary border-t-transparent rounded-full" />
              {progress}
            </div>
          </div>
        )}
      </main>

      <footer className="border-t py-6 text-center text-xs text-muted-foreground">
        <p>ResumeScanner — Free ATS Resume Analyzer. MIT License.</p>
      </footer>
    </div>
  )
}
