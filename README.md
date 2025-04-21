# ChainResumé: AI & Blockchain Resume Analyzer

## Project Overview
ChainResumé is an innovative project that utilizes Artificial Intelligence (AI) and Blockchain technology to evaluate resumes. This project combines the power of machine learning to score resumes based on predefined keywords and leverages blockchain for secure and transparent storage of evaluation results.

## Problem Statement
The job market today is flooded with resumes, making it difficult for recruiters to find the best match quickly. Traditional resume evaluation methods are time-consuming and prone to human bias. This project aims to automate resume evaluation using AI and ensure transparency with blockchain.

## Objective
1. **AI-Based Resume Scoring**: Implement an AI algorithm to evaluate resumes based on predefined keywords such as skills, experience, and education.
2. **Blockchain Integration**: Store the resume evaluation results on a blockchain to ensure transparency and immutability.

## Methodology
1. **Resume Scoring**: Using Python and the **TF-IDF Vectorizer** from the **scikit-learn** library, we analyze resumes and score them based on keywords related to specific job requirements (e.g., Python, Machine Learning).
2. **Blockchain Integration**: A Solidity-based smart contract will be used to store the resume evaluation result on the blockchain. (This feature is optional and will be implemented as the project progresses.)

## Features
- **Resume Analysis**: Extract text from resumes and analyze them to generate scores based on predefined keywords.
- **Blockchain Storage**: Store evaluation results on a blockchain for secure and transparent access.

## Tools & Technologies
- **Python**: For AI-based resume analysis.
- **PyPDF2**: To extract text from resume PDFs.
- **scikit-learn**: For building the machine learning model.
- **Solidity**: For smart contract creation (Blockchain integration).

## How to Run the Code
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/ChainResumé-AI-Blockchain-Resume-Analyzer.git
    cd ChainResumé-AI-Blockchain-Resume-Analyzer
    ```
2. Install the required Python libraries:
    ```bash
    pip install PyPDF2 scikit-learn
    ```
3. Run the Python script:
    ```bash
    python main.py
    ```

## Future Enhancements
- **Advanced AI Models**: Integrate more sophisticated AI models to improve resume scoring.
- **Blockchain Integration**: Implement the smart contract to store evaluation results on the blockchain.
- **Web Interface**: Develop a web app to upload and evaluate resumes in real-time.

---

### **Step 2: Push Changes to GitHub**

Once you’ve updated your **README.md**, push the changes to GitHub.

Here’s how you can do it:

1. Open your terminal/command prompt and navigate to your project directory.
2. Run the following commands to add, commit, and push the changes to GitHub:
   
   ```bash
   git add README.md
   git commit -m "Updated README with project details"
   git push origin main
