# ai-resume-evaluator
Edwisely - Evaluation
# AI Resume Evaluator

## Overview
An AI-powered system that evaluates resumes against a job description and generates a fit score.

## Features
- Upload multiple resumes
- Analyze against job description
- Candidate ranking
- Skill matching
- Strengths and gaps identification

## Tech Stack
- Frontend: ReactJS
- Backend: FastAPI (Python)
- LLM: Groq (LLaMA)

## How to Run

### Backend
cd backend  
uvicorn app.main:app --reload  

### Frontend
cd frontend  
npm start  

## Output
- Fit Score (0–100)
- Ranking of candidates
- Strengths and missing skills
