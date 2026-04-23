def calculate_score(match_data, experience_years):
    required_total = len(match_data["matched_required"]) + len(match_data["missing_required"])

    if required_total == 0:
        skill_score = 0
    else:
        skill_score = len(match_data["matched_required"]) / required_total * 100

    preferred_bonus = len(match_data["matched_preferred"]) * 5

    # Experience scoring (simple logic)
    if experience_years >= 5:
        exp_score = 100
    elif experience_years >= 2:
        exp_score = 70
    else:
        exp_score = 40

    final_score = (0.6 * skill_score + 0.3 * exp_score + 0.1 * preferred_bonus)

    return round(final_score, 2)