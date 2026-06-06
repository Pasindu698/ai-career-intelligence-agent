# AI Career Intelligence Agent

## Overview

AI Career Intelligence Agent is a smart resume analysis platform that helps job seekers evaluate their resumes against job descriptions. The system calculates an ATS-style match score, identifies missing skills, generates learning recommendations, recommends suitable career paths, and produces downloadable career reports.

This project was developed using Python and Streamlit to provide an interactive career intelligence solution for students, graduates, and professionals seeking to improve their employability.

---

## Features

### Resume Analysis

* Upload Resume PDF files
* Extract text automatically from resumes
* Identify technical and professional skills

### Job Description Analysis

* Analyze job descriptions
* Extract required skills automatically
* Compare resume skills with job requirements

### ATS Match Score

* Calculate ATS-style compatibility score
* Evaluate how well a resume matches a target role

### Skill Gap Analysis

* Identify missing skills
* Highlight areas for improvement

### Learning Roadmap

* Generate personalized learning recommendations
* Suggest technologies and skills to learn

### Strengths and Weaknesses Analysis

* Identify strong skill areas
* Highlight weaknesses based on target job requirements

### Career Role Recommendation Engine

* Recommend suitable career paths
* Match resumes with multiple career roles
* Display role match percentages

### PDF Career Report

* Generate downloadable career reports
* Include ATS score, strengths, weaknesses, missing skills, and recommendations

### Professional Web Interface

* User-friendly Streamlit dashboard
* Interactive analysis workflow

---

## Technologies Used

### Programming Language

* Python

### Libraries and Frameworks

* Streamlit
* PyPDF
* Pandas
* NumPy
* Scikit-Learn
* ReportLab
* Python Dotenv
* NLTK

### Version Control

* Git
* GitHub

---

## System Workflow

1. Upload Resume PDF
2. Extract Resume Text
3. Extract Resume Skills
4. Paste Job Description
5. Extract Job Description Skills
6. Calculate ATS Match Score
7. Identify Missing Skills
8. Generate Learning Recommendations
9. Generate Strengths and Weaknesses Analysis
10. Recommend Suitable Career Roles
11. Generate Downloadable PDF Career Report

---

## Project Structure

```text
ai-career-intelligence-agent/
│
├── data/
│   └── resumes/
│
├── src/
│   ├── pdf_reader.py
│   ├── skill_extractor.py
│   ├── matcher.py
│   ├── report_generator.py
│   └── role_recommender.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Pasindu698/ai-career-intelligence-agent.git
```

Navigate to the project folder:

```bash
cd ai-career-intelligence-agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Example Outputs

### ATS Match Score

```text
ATS Match Score: 90%
```

### Missing Skills

```text
- AWS
- Pandas
```

### Recommended Career Roles

```text
Data Analyst - 95%
Business Analyst - 88%
Data Scientist - 82%
Machine Learning Engineer - 74%
```

---

## Future Enhancements

* Fuzzy Skill Matching for spelling mistakes
* AI-powered Resume Feedback using LLMs
* RAG-based Career Advisor
* Personalized Learning Paths
* Interview Preparation Assistant
* Job Recommendation System
* Streamlit Cloud Deployment
* Authentication and User Profiles

---

## Author

Pasindu Edirisingha

Data Science Undergraduate
Sri Lanka Institute of Information Technology (SLIIT)

GitHub:
https://github.com/Pasindu698

LinkedIn:
https://www.linkedin.com

```
```
