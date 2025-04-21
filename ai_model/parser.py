import PyPDF2

def parse_resume(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    # Simple logic: count keywords
    score = 0
    feedback = []

    if 'Python' in text:
        score += 20
        feedback.append('Python skills found')
    if 'C++' in text:
        score += 20
        feedback.append('C++ mentioned')
    if 'project' in text.lower():
        score += 20
        feedback.append('Project experience found')
    if 'intern' in text.lower():
        score += 20
        feedback.append('Internship experience mentioned')
    if 'communication' in text.lower():
        score += 20
        feedback.append('Soft skills mentioned')

    total_score = min(score, 100)
    return total_score, feedback
