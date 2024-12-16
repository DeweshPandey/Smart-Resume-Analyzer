
from dotenv import load_dotenv

load_dotenv()


import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure( api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content , prompt):
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input , pdf_content[0], prompt])
    return response.text     


def input_pdf_setup(uploaded_file):
    
    if uploaded_file is not None:
        # convert pdf to image
        images = pdf2image.convert_from_bytes( uploaded_file.read())
        
        first_page = images[0]
        
        # convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format = "JPEG")
        img_byte_arr = img_byte_arr.getvalue()
        
        pdf_parts =[
            {
                "mime_type" : "image/jpeg" ,
                "data" : base64.b64encode(img_byte_arr).decode() 
                # encode to base64
            }
        ]
        
        return pdf_parts
    else:
        raise FileNotFoundError("No file Uploaded")
    

# Streamlit app

st.set_page_config(page_title = "ATS Resume Expert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description: ", key = "input")
uploaded_file= st.file_uploader("Upload your Resume(PDF).....", type = ["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")
    
submit1 = st.button("Tell Me About the Resume")
# submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("Percentage match")

# input_prompt1 = """
# You are an experienced Technical HR Manager with expertise in one of the following job roles: Data Science, Full Stack Web Development, Big Data Engineering, DevOps, or Data Analyst. Your task is to evaluate the provided resume against the job description for these roles. 

# Please provide your professional evaluation on whether the candidate’s profile aligns with the specified job role.  
# - Highlight the key strengths and weaknesses in the candidate's profile.  
# - Indicate areas where the candidate meets or fails to meet the job requirements.  
# - Present your evaluation in bullet points, including both critical points of acceptance and rejection.

# """

input_prompt1 = """
You are an AI-powered Resume Evaluation Expert with extensive experience in reviewing technical resumes for the following job roles: Data Science, Full Stack Web Development, Big Data Engineering, DevOps, and Data Analyst.

Your task is to evaluate the provided resume against the job description for one of these roles. Follow these structured steps to complete your evaluation:

1. **Alignment Check**: 
   - Review the resume and job description to determine if the candidate’s skills and experiences align with the role.
   - Provide a clear assessment of whether the resume meets the key qualifications of the job.

2. **Strengths**:
   - Highlight the top 3 strengths of the candidate’s profile that are directly relevant to the job description. 

3. **Weaknesses**:
   - Identify the key weaknesses or gaps in the resume that might prevent the candidate from qualifying for the job.

4. **Critical Points**:
   - List critical points where the candidate either qualifies or does not qualify for the job (e.g., missing essential skills or certifications).
   
Please provide your evaluation in bullet points for clarity, ensuring each point is clear and concise.
"""


# input_prompt3 = """
# You are an ATS (Applicant Tracking System) expert with a deep understanding of one of the following roles: Data Science, Full Stack Web Development, Big Data Engineering, DevOps, or Data Analyst. Your task is to evaluate the provided resume against the job description.

# Please output the following:  
# 1. **Percentage Match**: Provide the percentage of alignment between the resume and the job description.  
# 2. **Missing Keywords**: List the key skills and keywords missing from the resume that are essential for this role according to the job description.  
# 3. **Critical Gaps**: Highlight any significant gaps in the candidate’s qualifications that would likely result in rejection.  
# 4. **Key Strengths**: Mention the top strengths that match the job description for potential acceptance.  
# """

input_prompt3 ="""
You are an AI-powered ATS (Applicant Tracking System) evaluator with expertise in reviewing resumes for roles such as Data Science, Full Stack Web Development, Big Data Engineering, DevOps, or Data Analyst. Your task is to evaluate the resume against the provided job description, with a focus on ATS functionality.

Please follow these steps to evaluate the resume:

1. **Percentage Match**:
   - Analyze the alignment between the resume and the job description.
   - Output the percentage match based on how well the resume fits the job description, considering key skills, experience, and keywords.

2. **Missing Keywords**:
   - Identify any key skills or technical terms that are missing in the resume, but are present in the job description.
   - List these missing keywords in a bullet point format.

3. **Critical Gaps**:
   - Highlight any major gaps in the candidate’s qualifications that would likely lead to rejection by an ATS system.

4. **Key Strengths**:
   - Mention the top strengths of the candidate’s resume that are a strong match for the job description and would pass through an ATS.

Please provide your feedback in the following format:
- **Percentage Match**: [Match %]
- **Missing Keywords**: [List of keywords]
- **Critical Gaps**: [List of gaps]
- **Key Strengths**: [List of strengths]
"""
    
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        
        response = get_gemini_response( input_text , pdf_content , input_prompt1 )
        st.subheader("The Response is :")
        st.write(response)

    else:
        st.write("Please upload the resume")
        
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        
        response = get_gemini_response( input_text , pdf_content , input_prompt3 )
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write("Please upload the resume")