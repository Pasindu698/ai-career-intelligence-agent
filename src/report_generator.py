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