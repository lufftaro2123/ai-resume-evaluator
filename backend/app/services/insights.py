def generate_insights(match_data):
    strengths = []
    gaps = []

    # Strengths
    if match_data["matched_required"]:
        strengths.append(
            "Strong in " + ", ".join(match_data["matched_required"])
        )
    else:
        strengths.append("No strong required skills matched")

    if match_data["matched_preferred"]:
        strengths.append(
            "Also knows " + ", ".join(match_data["matched_preferred"])
        )

    # Gaps
    if match_data["missing_required"]:
        gaps.append(
            "Missing " + ", ".join(match_data["missing_required"])
        )
    else:
        gaps.append("No major skill gaps")

    return {
        "strengths": strengths,
        "gaps": gaps
    }