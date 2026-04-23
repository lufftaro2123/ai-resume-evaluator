from app.services.groq_service import call_groq
from app.utils.helpers import clean_json_response

def extract_jd_data(jd_text: str):
    prompt = f"""
    Extract structured data from this Job Description.

    Return ONLY valid JSON:
    {{
      "required_skills": [],
      "preferred_skills": [],
      "role_expectations": []
    }}

    JD:
    {jd_text}
    """

    response = call_groq(prompt)
    return clean_json_response(response)