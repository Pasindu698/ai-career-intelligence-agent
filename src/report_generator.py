def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        if skill == "pandas":
            recommendations.append(
                "Learn Pandas for data cleaning, EDA, and dataframe operations."
            )

        elif skill == "aws":
            recommendations.append(
                "Learn AWS Cloud Practitioner fundamentals, S3, and EC2."
            )

        elif skill == "python":
            recommendations.append(
                "Improve Python programming, file handling, functions, and OOP concepts."
            )

        elif skill == "sql":
            recommendations.append(
                "Practice joins, subqueries, aggregation, and window functions."
            )

        elif skill == "machine learning":
            recommendations.append(
                "Study regression, classification, model evaluation, and feature engineering."
            )

        elif skill == "power bi":
            recommendations.append(
                "Build dashboards, KPI reports, and learn DAX calculations."
            )

        else:
            recommendations.append(
                f"Learn {skill} because it is required in the target role."
            )

    return recommendations

def generate_strengths(cv_skills):

    strengths = []

    if "python" in cv_skills:
        strengths.append("Strong Python programming skills")

    if "sql" in cv_skills:
        strengths.append("Good database and SQL knowledge")

    if "power bi" in cv_skills:
        strengths.append("Experience with Business Intelligence and dashboards")

    if "machine learning" in cv_skills:
        strengths.append("Knowledge of Machine Learning concepts")

    if "git" in cv_skills and "github" in cv_skills:
        strengths.append("Version control and collaboration experience")

    return strengths


def generate_weaknesses(missing_skills):

    weaknesses = []

    for skill in missing_skills:
        weaknesses.append(f"Missing skill: {skill}")

    return weaknesses


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def create_pdf_report(score, cv_skills, jd_skills, missing_skills, recommendations, strengths, weaknesses):
    file_path = "career_report.pdf"

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 50

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "AI Career Intelligence Report")

    y -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"ATS Match Score: {score}%")

    y -= 35
    c.drawString(50, y, "CV Skills:")
    c.setFont("Helvetica", 10)

    for skill in cv_skills:
        y -= 18
        c.drawString(70, y, f"- {skill}")

    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Missing Skills:")
    c.setFont("Helvetica", 10)

    for skill in missing_skills:
        y -= 18
        c.drawString(70, y, f"- {skill}")

    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Strengths:")
    c.setFont("Helvetica", 10)

    for strength in strengths:
        y -= 18
        c.drawString(70, y, f"- {strength}")

    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Weaknesses:")
    c.setFont("Helvetica", 10)

    for weakness in weaknesses:
        y -= 18
        c.drawString(70, y, f"- {weakness}")

    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Learning Roadmap:")
    c.setFont("Helvetica", 10)

    for recommendation in recommendations:
        y -= 18
        c.drawString(70, y, f"- {recommendation}")

    c.save()

    return file_path