def resume_prompt(resume, job_description):

    return f"""
You are an ATS Resume Analyzer.

Analyze the resume against the job description.

Provide:

1. ATS Score out of 100

2. Matching Skills

3. Missing Skills

4. Resume Summary

5. Suggestions to Improve Resume

Resume:
{resume}

Job Description:
{job_description}
"""