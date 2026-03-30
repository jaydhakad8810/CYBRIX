const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export async function analyzeInput(mode, content) {
  const endpoint = mode === "message" ? "/analyze/message" : "/analyze/link";

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ content }),
  });

  if (!response.ok) {
    throw new Error("Unable to fetch analysis result from the backend.");
  }

  return response.json();
}
