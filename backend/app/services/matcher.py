def match_skills(resume_skills, required_skills, preferred_skills):
    resume_skills = set([s.lower() for s in resume_skills])
    required_skills = set([s.lower() for s in required_skills])
    preferred_skills = set([s.lower() for s in preferred_skills])

    matched_required = resume_skills.intersection(required_skills)
    missing_required = required_skills - resume_skills

    matched_preferred = resume_skills.intersection(preferred_skills)

    return {
        "matched_required": list(matched_required),
        "missing_required": list(missing_required),
        "matched_preferred": list(matched_preferred)
    }