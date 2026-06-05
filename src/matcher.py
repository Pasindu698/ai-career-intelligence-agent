def calculate_match_score(cv_skills, jd_skills):
    if len(jd_skills) == 0:
        return 0

    matched_skills = []

    for skill in jd_skills:
        if skill in cv_skills:
            matched_skills.append(skill)

    score = (len(matched_skills) / len(jd_skills)) * 100

    return round(score, 2)


def find_missing_skills(cv_skills, jd_skills):
    missing_skills = []

    for skill in jd_skills:
        if skill not in cv_skills:
            missing_skills.append(skill)

    return missing_skills