import streamlit as st

from utils.pdf_reader import extract_text
from utils.prompts import resume_prompt
from utils.gemini_helper import get_response

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if uploaded_file and job_description:

        resume_text = extract_text(
            uploaded_file
        )

        prompt = resume_prompt(
            resume_text,
            job_description
        )

        result = get_response(prompt)

        st.markdown(result)

    else:
        st.warning(
            "Upload Resume and Job Description"
        )