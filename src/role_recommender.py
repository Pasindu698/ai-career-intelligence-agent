ROLE_SKILLS = {
    "Data Analyst": [
        "python", "sql", "excel", "power bi", "data analysis", "data visualization"
    ],
    "Business Analyst": [
        "excel", "sql", "power bi", "data analysis", "data visualization"
    ],
    "Data Scientist": [
        "python", "sql", "machine learning", "pandas", "numpy", "data analysis"
    ],
    "Machine Learning Engineer": [
        "python", "machine learning", "scikit-learn", "tensorflow", "pytorch", "docker"
    ],
    "BI Analyst": [
        "sql", "power bi", "excel", "data visualization", "data analysis"
    ],
    "Full Stack Developer": [
        "react", "node.js", "mongodb", "mysql", "git", "github"
    ]
}


def recommend_roles(cv_skills):
    recommendations = []

    for role, required_skills in ROLE_SKILLS.items():
        matched_skills = []

        for skill in required_skills:
            if skill in cv_skills:
                matched_skills.append(skill)

        score = (len(matched_skills) / len(required_skills)) * 100

        recommendations.append({
            "role": role,
            "score": round(score, 2),
            "matched_skills": matched_skills,
            "missing_skills": [
                skill for skill in required_skills if skill not in cv_skills
            ]
        })

    recommendations.sort(key=lambda x: x["score"], reverse=True)

    return recommendations