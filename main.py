import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Example keywords for resume scoring (skills, experience, etc.)
keywords = ["Python", "Data Science", "Machine Learning", "AI", "Deep Learning"]

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def score_resume(resume_text):
    # Simple scoring system based on keyword frequency
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([resume_text])
    feature_names = vectorizer.get_feature_names_out()
    
    # Count keywords in the resume
    score = 0
    for keyword in keywords:
        if keyword.lower() in resume_text.lower():
            score += 1
    
    return score

if __name__ == "__main__":
    resume_path = "sample_resume.pdf"  # Replace with your sample resume file
    resume_text = extract_text_from_pdf(resume_path)
    score = score_resume(resume_text)
    print(f"Resume Score: {score}/5")
