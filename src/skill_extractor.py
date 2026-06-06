SKILL_KEYWORDS = {
    "python": ["python"],
    "sql": ["sql"],
    "power bi": ["power bi", "powerbi"],
    "excel": ["excel", "ms excel", "microsoft excel"],
    "machine learning": ["machine learning", "ml"],
    "data analysis": ["data analysis", "data analytics", "analytics", "eda", "exploratory data analysis"],
    "data visualization": ["data visualization", "data visualisation", "dashboard", "dashboards"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "react": ["react", "react.js", "reactjs"],
    "node.js": ["node.js", "nodejs", "node"],
    "mongodb": ["mongodb", "mongo db"],
    "mysql": ["mysql", "my sql"],
    "git": ["git"],
    "github": ["github"],
    "docker": ["docker"],
    "aws": ["aws", "amazon web services"],
}

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill, keywords in SKILL_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                found_skills.append(skill)
                break

    return found_skills