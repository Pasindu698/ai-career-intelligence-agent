SKILLS = [
    "python",
    "sql",
    "power bi",
    "excel",
    "machine learning",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "react",
    "node.js",
    "mongodb",
    "mysql",
    "git",
    "github",
    "docker"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return found_skills