# 📄 ATS Resume Expert

An AI-powered web application built with **Streamlit** and **Google Gemini API** to evaluate resumes against job descriptions, providing insights on strengths, weaknesses, critical gaps, and ATS (Applicant Tracking System) alignment.

## 🚀 Features
- Upload your PDF resume and match it against a job description.
- Receive AI-generated feedback on alignment, strengths, weaknesses, and missing keywords.
- Get an ATS percentage match score for improved resume optimization.

## 🛠️ Technologies & Libraries Used
- **Streamlit**: For building the web-based user interface.
- **Pillow (PIL)**: Image processing for PDF conversion.
- **pdf2image**: Converts PDF pages into images.
- **Google Generative AI (Gemini API)**: AI-driven text analysis and resume evaluation.
- **dotenv**: Manages environment variables securely.
- **os & io**: File and input/output operations.
- **base64**: Encoding PDF images for API compatibility.

## 📦 Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ats-resume-expert.git
cd ats-resume-expert
```

2. Create a `.env` file and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

3. Install the dependencies:
```bash
pip install streamlit pillow pdf2image google-generativeai python-dotenv
```

4. Run the application:
```bash
streamlit run app.py
```

## 📊 How It Works
1. Enter the **Job Description** in the text area.
2. Upload your **Resume (PDF format)**.
3. Click on **"Tell Me About the Resume"** or **"Percentage Match"**.
4. View AI-generated insights and ATS alignment.

## 📚 Prompts Used
- **Evaluation Prompt**: Provides strengths, weaknesses, and critical analysis.
- **ATS Match Prompt**: Calculates percentage match, missing keywords, and gaps.

## 🤝 Contributions
Feel free to fork, contribute, or report issues.

## 📄 License
This project is licensed under the **MIT License**.

## 📬 Contact
For feedback or queries, reach out at **your.email@example.com**.

---
**Enhance your resume. Match your dream job. 🚀**
****
