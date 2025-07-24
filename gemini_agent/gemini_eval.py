import google.generativeai as genai
from .prompts import SYSTEM_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_evaluation(summary: str, rows) -> str:
    prompt = SYSTEM_PROMPT
    wikipedia_text = " ".join(row[0] for row in rows)
    rag_data = f"{{ 'wikipedia': \"{wikipedia_text}\" }}"
    full_prompt = prompt + "\n\n" + summary + "\n\n" + rag_data
    return model.generate_content(full_prompt).text
