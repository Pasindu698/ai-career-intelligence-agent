import streamlit as st
import pandas as pd

from src.pdf_reader import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.matcher import calculate_match_score, find_missing_skills
from src.report_generator import (
    generate_recommendations,
    generate_strengths,
    generate_weaknesses,
    generate_resume_feedback,
    create_pdf_report
)
from src.role_recommender import recommend_roles

st.set_page_config(
    page_title="AI Career Intelligence Agent",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 45%, #020617 100%);
    color: #f8fafc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero-card {
    background: rgba(255, 255, 255, 0.08);
    padding: 28px;
    border-radius: 22px;
    border: 1px solid rgba(255, 255, 255, 0.14);
    box-shadow: 0 20px 45px rgba(0,0,0,0.25);
    margin-bottom: 25px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 18px;
    color: #cbd5e1;
}

.result-card {
    background: rgba(255, 255, 255, 0.09);
    padding: 22px;
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.14);
    margin-bottom: 18px;
}

.metric-card {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    padding: 22px;
    border-radius: 18px;
    text-align: center;
    color: white;
    box-shadow: 0 16px 35px rgba(37, 99, 235, 0.25);
}

.metric-value {
    font-size: 34px;
    font-weight: 800;
}

.metric-label {
    font-size: 14px;
    opacity: 0.9;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 12px;
}

.skill-pill {
    display: inline-block;
    background: rgba(59, 130, 246, 0.18);
    color: #bfdbfe;
    padding: 8px 12px;
    margin: 5px;
    border-radius: 999px;
    border: 1px solid rgba(147, 197, 253, 0.25);
    font-size: 14px;
}

.missing-pill {
    display: inline-block;
    background: rgba(239, 68, 68, 0.18);
    color: #fecaca;
    padding: 8px 12px;
    margin: 5px;
    border-radius: 999px;
    border: 1px solid rgba(252, 165, 165, 0.25);
    font-size: 14px;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    padding: 12px;
    font-weight: 700;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    border: none;
}

.stDownloadButton > button {
    width: 100%;
    border-radius: 12px;
    padding: 12px;
    font-weight: 700;
    background: linear-gradient(135deg, #16a34a, #22c55e);
    color: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-card">
    <div class="hero-title">🚀 AI Career Intelligence Agent</div>
    <div class="hero-subtitle">
        Upload your resume, paste a job description, and get an ATS match score,
        missing skills, career role recommendations, learning roadmap, and a downloadable report.
    </div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("⚙️ Dashboard")
    st.write("Smart resume and job description analyzer for career preparation.")

    st.markdown("---")
    st.subheader("Features")
    st.write("✅ ATS Match Score")
    st.write("✅ Skill Gap Analysis")
    st.write("✅ Learning Roadmap")
    st.write("✅ Strengths & Weaknesses")
    st.write("✅ Role Recommendations")
    st.write("✅ PDF Career Report")

    st.markdown("---")
    st.caption("Built with Python, Streamlit, PyPDF, and ReportLab.")

left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.subheader("📄 Upload Resume")
    uploaded_cv = st.file_uploader("Upload your CV PDF", type=["pdf"])

with right_col:
    st.subheader("🧾 Job Description")
    job_description = st.text_area(
        "Paste Job Description",
        height=180,
        placeholder="Paste the full job description here..."
    )

analyze_button = st.button("Analyze Career Match")

if analyze_button:
    if uploaded_cv is None:
        st.error("Please upload your CV PDF.")

    elif job_description.strip() == "":
        st.error("Please paste a job description.")

    else:
        with open("data/resumes/uploaded_cv.pdf", "wb") as file:
            file.write(uploaded_cv.getbuffer())

        cv_text = extract_text_from_pdf("data/resumes/uploaded_cv.pdf")

        cv_skills = extract_skills(cv_text)
        jd_skills = extract_skills(job_description)

        score = calculate_match_score(cv_skills, jd_skills)
        missing_skills = find_missing_skills(cv_skills, jd_skills)
        recommendations = generate_recommendations(missing_skills)
        strengths = generate_strengths(cv_skills)
        weaknesses = generate_weaknesses(missing_skills)
        role_recommendations = recommend_roles(cv_skills)
        resume_feedback = generate_resume_feedback(score, missing_skills, cv_skills)

        st.success("Analysis completed successfully!")

        m1, m2, m3 = st.columns(3)

        with m1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{score}%</div>
                    <div class="metric-label">ATS Match Score</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with m2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{len(cv_skills)}</div>
                    <div class="metric-label">CV Skills Found</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with m3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{len(jd_skills)}</div>
                    <div class="metric-label">JD Skills Required</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">📊 Skill Match Overview</div>', unsafe_allow_html=True)

            matched_count = len(jd_skills) - len(missing_skills)

            skill_chart_data = pd.DataFrame({
                "Category": ["Matched Skills", "Missing Skills"],
                "Count": [matched_count, len(missing_skills)]
            })

            st.bar_chart(skill_chart_data.set_index("Category"))

            st.markdown('</div>', unsafe_allow_html=True)

        with chart_col2:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">🎯 Career Role Match Scores</div>', unsafe_allow_html=True)

            role_chart_data = pd.DataFrame({
                "Role": [role["role"] for role in role_recommendations[:5]],
                "Score": [role["score"] for role in role_recommendations[:5]]
            })

            st.bar_chart(role_chart_data.set_index("Role"))

            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">✅ Skills Found in Your CV</div>', unsafe_allow_html=True)
        if cv_skills:
            st.markdown(
                " ".join([f'<span class="skill-pill">{skill}</span>' for skill in cv_skills]),
                unsafe_allow_html=True
            )
        else:
            st.info("No skills detected in your CV.")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📌 Skills Required in Job Description</div>', unsafe_allow_html=True)
        if jd_skills:
            st.markdown(
                " ".join([f'<span class="skill-pill">{skill}</span>' for skill in jd_skills]),
                unsafe_allow_html=True
            )
        else:
            st.info("No skills detected in the job description.")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">⚠️ Missing Skills</div>', unsafe_allow_html=True)
        if missing_skills:
            st.markdown(
                " ".join([f'<span class="missing-pill">{skill}</span>' for skill in missing_skills]),
                unsafe_allow_html=True
            )
        else:
            st.success("No missing skills found!")
        st.markdown('</div>', unsafe_allow_html=True)

        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">💪 Strengths</div>', unsafe_allow_html=True)
            if strengths:
                for strength in strengths:
                    st.success(strength)
            else:
                st.info("No major strengths detected yet.")
            st.markdown('</div>', unsafe_allow_html=True)

        with col_b:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">⚠ Weaknesses</div>', unsafe_allow_html=True)
            if weaknesses:
                for weakness in weaknesses:
                    st.warning(weakness)
            else:
                st.success("No major weaknesses found.")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📚 Learning Roadmap</div>', unsafe_allow_html=True)
        if recommendations:
            for recommendation in recommendations:
                st.write("•", recommendation)
        else:
            st.success("Excellent! No major skill gaps found.")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🎯 Recommended Career Roles</div>', unsafe_allow_html=True)

        for role in role_recommendations[:4]:
            st.write(f"**{role['role']}** - {role['score']}% match")
            st.progress(role["score"] / 100)
            st.caption(f"Matched skills: {', '.join(role['matched_skills'])}")

            if role["missing_skills"]:
                st.caption(f"Missing skills: {', '.join(role['missing_skills'])}")

            st.write("---")

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🤖 Resume Improvement Suggestions</div>', unsafe_allow_html=True)

        for feedback in resume_feedback:
            st.info(feedback)

        st.markdown('</div>', unsafe_allow_html=True)

        pdf_path = create_pdf_report(
            score,
            cv_skills,
            jd_skills,
            missing_skills,
            recommendations,
            strengths,
            weaknesses
        )

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Download Career Report PDF",
                data=pdf_file,
                file_name="career_report.pdf",
                mime="application/pdf"
            )