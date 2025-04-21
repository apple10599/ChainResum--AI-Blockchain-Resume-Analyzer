from flask import Flask, render_template, request
import os
from ai_model.parser import analyze_resume

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_file = request.files["resume"]
        if resume_file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(filepath)

            # Analyze resume (mock AI logic here)
            score, feedback = analyze_resume(filepath)

            return render_template("index.html", score=score, feedback=feedback, filename=resume_file.filename)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

