import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def generate_gemini_feedback(cv_text, job_description, score, missing_skills):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini API key not found."

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are an expert ATS reviewer and career coach.

Analyze the following resume and job description.

Resume:
{cv_text[:4000]}

Job Description:
{job_description[:3000]}

ATS Score:
{score}%

Missing Skills:
{missing_skills}

Provide:

1. Resume Strengths
2. Resume Weaknesses
3. Missing Skills Analysis
4. Resume Improvement Suggestions
5. Suggested Projects
6. Career Advice

Keep the answer concise and professional.
"""

    response = model.generate_content(prompt)

    return response.text