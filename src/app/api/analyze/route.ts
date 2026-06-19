import { NextRequest, NextResponse } from "next/server"

const API_BASE = process.env.NODE_ENV === "development"
  ? "http://localhost:8000"
  : ""

async function proxy(request: NextRequest, path: string): Promise<NextResponse> {
  try {
    const formData = await request.formData()
    const res = await fetch(`${API_BASE}${path}`, {
      method: "POST",
      body: formData,
    })
    const data = await res.json()
    return NextResponse.json(data, { status: res.status })
  } catch {
    return NextResponse.json(
      { error: "Local API server is not running. Run: source venv/bin/activate && python run_api.py" },
      { status: 503 }
    )
  }
}

export async function POST(request: NextRequest) {
  if (API_BASE) {
    return proxy(request, "/api/analyze")
  }
  return NextResponse.json(
    { error: "Production uses Vercel Python runtime. Deploy to Vercel or run in dev mode." },
    { status: 500 }
  )
}

export async function GET() {
  return NextResponse.json({ status: "ok", service: "ResumeScanner API" })
}
