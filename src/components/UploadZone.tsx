"use client"

import { Upload, FileText, X, Loader2 } from "lucide-react"
import { useRef, useState, type DragEvent, type ChangeEvent } from "react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { cn } from "@/lib/utils"

interface UploadZoneProps {
  onAnalyze: (file: File, jobDescription: string, domain: string) => void
  loading: boolean
  error: string | null
}

const MAX_FILE_SIZE = 5 * 1024 * 1024
const ALLOWED_TYPES = [".pdf", ".docx"]

const DOMAINS = [
  { key: "all", label: "Auto-detect (all domains)" },
  { key: "tech", label: "Technology & Software" },
  { key: "cloud", label: "Cloud & Infrastructure" },
  { key: "data", label: "Data & Analytics" },
  { key: "finance", label: "Banking & Finance" },
  { key: "insurance", label: "Insurance" },
  { key: "marketing", label: "Marketing & Sales" },
  { key: "healthcare", label: "Healthcare & Pharma" },
  { key: "engineering", label: "Engineering & Manufacturing" },
  { key: "automotive", label: "Automotive" },
  { key: "operations", label: "Operations & Supply Chain" },
  { key: "legal", label: "Legal & Regulatory" },
  { key: "hr", label: "HR & Recruitment" },
  { key: "creative", label: "Creative & Design" },
  { key: "education", label: "Education & Research" },
  { key: "government", label: "Government & Public Sector" },
  { key: "realestate", label: "Real Estate & Construction" },
  { key: "energy", label: "Energy & Utilities" },
  { key: "retail", label: "Retail & E-Commerce" },
  { key: "media", label: "Media & Entertainment" },
  { key: "hospitality", label: "Hospitality & Tourism" },
  { key: "agriculture", label: "Agriculture & Food" },
  { key: "aviation", label: "Aviation & Aerospace" },
]

export function UploadZone({ onAnalyze, loading, error }: UploadZoneProps) {
  const [file, setFile] = useState<File | null>(null)
  const [jobDescription, setJobDescription] = useState("")
  const [domain, setDomain] = useState("all")
  const [dragOver, setDragOver] = useState(false)
  const [localError, setLocalError] = useState<string | null>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const displayError = localError || error

  function validateFile(f: File): string | null {
    const ext = "." + f.name.split(".").pop()?.toLowerCase()
    if (!ALLOWED_TYPES.includes(ext)) {
      return "Invalid file type. Please upload a PDF or DOCX file."
    }
    if (f.size > MAX_FILE_SIZE) {
      return `File is too large (${(f.size / 1024 / 1024).toFixed(1)}MB). Maximum size is 5MB.`
    }
    return null
  }

  function handleFile(input: File) {
    setLocalError(null)
    const err = validateFile(input)
    if (err) {
      setLocalError(err)
      return
    }
    setFile(input)
  }

  function handleDrop(e: DragEvent) {
    e.preventDefault()
    setDragOver(false)
    const dropped = e.dataTransfer.files[0]
    if (dropped) handleFile(dropped)
  }

  function handleInputChange(e: ChangeEvent<HTMLInputElement>) {
    const selected = e.target.files?.[0]
    if (selected) handleFile(selected)
  }

  function handleSubmit() {
    if (!file) return
    onAnalyze(file, jobDescription, domain)
  }

  function clearFile() {
    setFile(null)
    setLocalError(null)
    if (fileInputRef.current) fileInputRef.current.value = ""
  }

  return (
    <div className="w-full max-w-2xl mx-auto space-y-6">
      <div
        onDragOver={(e) => { e.preventDefault(); setDragOver(true) }}
        onDragLeave={() => setDragOver(false)}
        onDrop={handleDrop}
        className={cn(
          "relative border-2 border-dashed rounded-xl p-10 text-center transition-colors cursor-pointer",
          dragOver
            ? "border-primary bg-primary/5"
            : file
              ? "border-emerald-500/50 bg-emerald-500/5"
              : "border-border hover:border-primary/50 hover:bg-muted/50",
          displayError && "border-destructive/50 bg-destructive/5"
        )}
        onClick={() => !file && fileInputRef.current?.click()}
      >
        <input
          ref={fileInputRef}
          type="file"
          accept=".pdf,.docx"
          onChange={handleInputChange}
          className="hidden"
        />

        {file ? (
          <div className="flex items-center justify-center gap-3">
            <FileText className="h-8 w-8 text-emerald-500" />
            <div className="text-left">
              <p className="font-semibold text-foreground">{file.name}</p>
              <p className="text-sm text-muted-foreground">
                {(file.size / 1024).toFixed(0)} KB
              </p>
            </div>
            <Button
              variant="ghost"
              size="icon"
              onClick={(e) => { e.stopPropagation(); clearFile() }}
              className="ml-4"
            >
              <X className="h-5 w-5" />
            </Button>
          </div>
        ) : (
          <>
            <Upload className="h-10 w-10 mx-auto mb-4 text-muted-foreground" />
            <p className="text-lg font-semibold text-foreground">
              Drop your resume here
            </p>
            <p className="text-sm text-muted-foreground mt-1">
              or click to browse — PDF or DOCX, max 5MB
            </p>
          </>
        )}
      </div>

      {displayError && (
        <div className="rounded-lg border border-destructive/50 bg-destructive/5 p-4 text-sm text-destructive">
          <p className="font-semibold">Error</p>
          <p>{displayError}</p>
          {displayError?.includes("Invalid file type") && (
            <p className="mt-1 text-muted-foreground">
              Only PDF and DOCX files are supported.
            </p>
          )}
          {displayError?.includes("too large") && (
            <p className="mt-1 text-muted-foreground">
              Try uploading a smaller file (under 5MB). Most resumes are 1-2MB.
            </p>
          )}
        </div>
      )}

      <div className="space-y-2">
        <label className="text-sm font-medium text-foreground">
          Industry Domain{" "}
          <span className="text-muted-foreground font-normal">(narrows search)</span>
        </label>
        <select
          value={domain}
          onChange={(e) => setDomain(e.target.value)}
          className="w-full rounded-lg border border-input bg-background px-3 py-2 text-sm ring-offset-background focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2"
        >
          {DOMAINS.map((d) => (
            <option key={d.key} value={d.key}>{d.label}</option>
          ))}
        </select>
      </div>

      <div className="space-y-2">
        <div className="flex items-center justify-between">
          <label className="text-sm font-medium text-foreground">
            Job Description{" "}
            <span className="text-muted-foreground font-normal">(optional)</span>
          </label>
          <JDUploadButton onText={(t) => setJobDescription(t)} />
        </div>
        <Textarea
          placeholder="Paste the job description here to match keywords and identify skill gaps..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          rows={5}
          maxLength={5000}
          className="resize-y min-h-[120px]"
        />
        <p className="text-xs text-muted-foreground text-right">
          {jobDescription.length}/5000 characters
        </p>
      </div>

      <Button
        onClick={handleSubmit}
        disabled={!file || loading}
        size="lg"
        className="w-full text-base font-semibold"
      >
        {loading ? (
          <span className="flex items-center gap-2">
            <span className="animate-spin h-4 w-4 border-2 border-current border-t-transparent rounded-full" />
            Analyzing...
          </span>
        ) : (
          "Analyze Resume"
        )}
      </Button>
    </div>
  )
}

function JDUploadButton({ onText }: { onText: (text: string) => void }) {
  const [parsing, setParsing] = useState(false)
  const jdInputRef = useRef<HTMLInputElement>(null)

  async function handleJDFile(e: ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0]
    if (!file) return
    setParsing(true)

    try {
      const formData = new FormData()
      formData.append("file", file)
      const res = await fetch("/api/parse", { method: "POST", body: formData })
      const data = await res.json()
      if (data.text) {
        onText(data.text.substring(0, 5000))
      }
    } catch {
      // silently fail
    } finally {
      setParsing(false)
      if (jdInputRef.current) jdInputRef.current.value = ""
    }
  }

  return (
    <>
      <input
        ref={jdInputRef}
        type="file"
        accept=".pdf,.docx"
        onChange={handleJDFile}
        className="hidden"
      />
      <Button
        type="button"
        variant="ghost"
        size="sm"
        className="text-xs gap-1.5 text-muted-foreground"
        onClick={() => jdInputRef.current?.click()}
        disabled={parsing}
      >
        {parsing ? (
          <Loader2 className="h-3 w-3 animate-spin" />
        ) : (
          <Upload className="h-3 w-3" />
        )}
        {parsing ? "Parsing..." : "Upload JD"}
      </Button>
    </>
  )
}
