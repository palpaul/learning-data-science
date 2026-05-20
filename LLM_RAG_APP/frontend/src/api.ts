// All API calls go through /api/* — Nginx (prod) or Vite proxy (dev)
// forwards them to the FastAPI backend on port 8000.
const API_BASE = '/api'

type ApiResponse<T = unknown> = Promise<T>

export async function uploadPdf(file: File): ApiResponse<unknown> {
  const formData = new FormData()
  formData.append('file', file)

  const res = await fetch(`${API_BASE}/upload-pdf/`, {
    method: 'POST',
    body: formData,
  })

  if (!res.ok) {
    const text = await res.text()
    throw new Error(`Upload failed (${res.status}): ${text}`)
  }

  return res.json()
}

export async function askQuestion(question: string): ApiResponse<unknown> {
  const url = `${API_BASE}/ask/?question=${encodeURIComponent(question)}`
  const res = await fetch(url)

  if (!res.ok) {
    const text = await res.text()
    throw new Error(`Request failed (${res.status}): ${text}`)
  }

  return res.json()
}

export async function viewData(): ApiResponse<unknown> {
  const res = await fetch(`${API_BASE}/view-data/`)
  if (!res.ok) {
    const text = await res.text()
    throw new Error(`Failed to fetch data (${res.status}): ${text}`)
  }

  return res.json()
}

export async function healthCheck(): ApiResponse<unknown> {
  const res = await fetch(`${API_BASE}/`)
  if (!res.ok) {
    const text = await res.text()
    throw new Error(`Backend not reachable (${res.status}): ${text}`)
  }

  return res.json()
}
