import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def call_groq(prompt: str):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f'{{"error": "LLM failed", "details": "{str(e)}"}}'


def extract_resume_data(resume_text: str):
    prompt = f"""
    Extract structured information from this resume.

    STRICTLY return valid JSON. No explanation.

    {{
      "skills": [],
      "experience_years": number,
      "projects": [],
      "education": ""
    }}

    Resume:
    {resume_text}
    """

    return call_groq(prompt)


def analyze_with_jd(resume_data, jd_text):
    prompt = f"""
    Analyze the candidate against the job description.

    STRICTLY return valid JSON.

    Resume Data:
    {resume_data}

    Job Description:
    {jd_text}

    {{
      "skill_match": number,
      "experience_match": number,
      "role_fit": number,
      "strengths": [],
      "gaps": []
    }}
    """

    return call_groq(prompt)