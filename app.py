import streamlit as st

from src.pdf_reader import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.matcher import calculate_match_score, find_missing_skills

st.set_page_config(
    page_title="AI Career Intelligence Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Intelligence Agent")
st.write("Upload your CV and paste a job description to analyze your career match.")

uploaded_cv = st.file_uploader("Upload your CV PDF", type=["pdf"])

job_description = st.text_area(
    "Paste Job Description",
    height=200,
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

        st.success("Analysis completed!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("ATS Match Score", f"{score}%")

        with col2:
            st.metric("CV Skills Found", len(cv_skills))

        with col3:
            st.metric("JD Skills Required", len(jd_skills))

        st.subheader("✅ Skills Found in Your CV")
        st.write(cv_skills)

        st.subheader("📌 Skills Required in Job Description")
        st.write(jd_skills)

        st.subheader("⚠️ Missing Skills")
        if missing_skills:
            st.write(missing_skills)
        else:
            st.success("No missing skills found!")