import os
import json
import time
from pathlib import Path
from google import genai
from google.genai import types
from pydantic import BaseModel
from dotenv import load_dotenv


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class TaskItem(BaseModel):
    description: str
    priority: str  
    estimated_minutes: int

class StudyPlanResponse(BaseModel):
    summary: str
    tasks: list[TaskItem]

def get_available_models() -> list[str]:
    
    preferred = ["gemini-3.8-flash", "gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-2.0-flash"]
    available = []
    try:
        for m in client.models.list():
            name = m.name.replace("models/", "")
            if "gemini" in name and "flash" in name and "tts" not in name and "image" not in name:
                available.append(name)
    except Exception:
        return preferred

    
    ordered = [m for m in preferred if m in available] + [m for m in available if m not in preferred]
    return ordered if ordered else preferred

def generate_study_plan(content: str) -> dict:
    prompt = f"""
    Analyze the following study notes or task list. 
    1. Provide a concise, clear summary (2-3 sentences).
    2. Break it down into actionable study tasks with a priority ('High', 'Medium', or 'Low') and estimated time in minutes.

    Content:
    {content}
    """

    models_to_try = get_available_models()
    last_error = None

    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=StudyPlanResponse,
                    temperature=0.3,
                ),
            )
            return json.loads(response.text)
        except Exception as e:
            last_error = e
            time.sleep(0.5)
            continue

    raise RuntimeError(f"AI request failed across models {models_to_try}. Last error: {last_error}")
