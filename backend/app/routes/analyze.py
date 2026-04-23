from fastapi import APIRouter, UploadFile, File, Form
from app.services.parser import extract_text_from_pdf
from app.services.groq_service import extract_resume_data
from app.services.jd_parser import extract_jd_data
from app.services.matcher import match_skills
from app.services.scorer import calculate_score
from app.utils.helpers import clean_json_response
from typing import List
from app.services.insights import generate_insights

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    resumes: List[UploadFile] = File(...),
    jd: str = Form(...)
):
    results = []

    # 1. Extract JD once
    jd_data = extract_jd_data(jd)

    for resume in resumes:
        # Extract text
        text = extract_text_from_pdf(resume.file)

        # Resume structured
        resume_raw = extract_resume_data(text)
        resume_data = clean_json_response(resume_raw)

        # Skill match
        match_data = match_skills(
            resume_data.get("skills", []),
            jd_data.get("required_skills", []),
            jd_data.get("preferred_skills", [])
        )

        # Score
        score = calculate_score(
            match_data,
            resume_data.get("experience_years", 0)
        )

        # Insights (NEW)
        insights = generate_insights(match_data)

        results.append({
            "filename": resume.filename,
            "score": score,
            "match_data": match_data,
            "insights": insights,
            "resume_data": resume_data
        })

    # 🔥 Ranking
    ranked_results = sorted(results, key=lambda x: x["score"], reverse=True)

    return {
        "ranking": ranked_results,
        "jd_data": jd_data
    }