import streamlit as st

from src.role_recommender import recommend_roles
from src.pdf_reader import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.matcher import calculate_match_score, find_missing_skills
from src.report_generator import (
    generate_recommendations,
    generate_strengths,
    generate_weaknesses,
    create_pdf_report
)

st.set_page_config(
    page_title="AI Career Intelligence Agent",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

.section-box {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Career Intelligence Agent")

st.markdown("""
### Smart Resume & Job Description Analyzer
Analyze your CV against a job description and receive an ATS score, missing skills, strengths, weaknesses, learning roadmap, and downloadable career report.
""")

with st.sidebar:
    st.header("📌 About")
    st.write("This AI Career Intelligence Agent helps job seekers evaluate their CV against job descriptions.")

    st.header("⚙️ Features")
    st.write("✅ ATS Match Score")
    st.write("✅ Missing Skills")
    st.write("✅ Learning Roadmap")
    st.write("✅ Strengths & Weaknesses")
    st.write("✅ PDF Career Report")

uploaded_cv = st.file_uploader("Upload your CV PDF", type=["pdf"])

job_description = st.text_area(
    "Paste Job Description",
    height=220,
    placeholder="Paste the full job description here..."
)

if st.button("Analyze"):
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

        st.success("Analysis completed!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("ATS Match Score", f"{score}%")

        with col2:
            st.metric("CV Skills Found", len(cv_skills))

        with col3:
            st.metric("JD Skills Required", len(jd_skills))

        st.divider()

        st.subheader("✅ Skills Found in Your CV")
        st.write(cv_skills)

        st.subheader("📌 Skills Required in Job Description")
        st.write(jd_skills)

        st.subheader("⚠️ Missing Skills")

        if missing_skills:
            st.write(missing_skills)
        else:
            st.success("No missing skills found!")

        st.subheader("💪 Strengths")

        if strengths:
            for strength in strengths:
                st.success(strength)
        else:
            st.info("No major strengths detected yet.")

        st.subheader("⚠ Weaknesses")

        if weaknesses:
            for weakness in weaknesses:
                st.warning(weakness)
        else:
            st.success("No major weaknesses found.")

        st.subheader("📚 Learning Roadmap")

        if recommendations:
            for recommendation in recommendations:
                st.write("•", recommendation)
        else:
            st.success("Excellent! No major skill gaps found.")

        st.subheader("🎯 Recommended Career Roles")

        for role in role_recommendations[:4]:
            st.write(f"**{role['role']}** - {role['score']}% match")
            st.progress(role["score"] / 100)
            st.caption(f"Matched skills: {', '.join(role['matched_skills'])}")

            if role["missing_skills"]:
                st.caption(f"Missing skills: {', '.join(role['missing_skills'])}")

            st.write("---")
            
        st.divider()

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