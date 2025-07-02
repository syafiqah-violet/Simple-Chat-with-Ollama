from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:8000"]
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return {"response": result["response"]}
