import os
import subprocess
from datetime import datetime
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "a-random-secret-key")

# Ensure the upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {"png", "jpg", "jpeg", "gif", "bmp", "pdf"}

def query_openai(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
    return "An error occurred while querying the AI."

def generate_latex_document(vuln_name, hostname, vuln_desc, poc, vuln_impact, vuln_mitigation, saved_files):
    latex_content = r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\begin{document}
\title{Vulnerability Report: %s}
\date{%s}
\maketitle
\newpage
\section*{Hostname/FQDN}
%s
\section*{Vulnerability Description}
%s
\section*{Proof of Concept}
%s
\section*{Vulnerability Impact}
%s
\section*{Mitigation Steps}
%s
\newpage
\section*{Attachments}
""" % (
        vuln_name,
        datetime.now().strftime("%Y-%m-%d"),
        hostname,  # Include hostname here
        vuln_desc,
        poc,
        vuln_impact,
        vuln_mitigation,
    )

    for image_path in saved_files:
        latex_content += r"""\begin{figure}[h!]
\centering
\includegraphics[width=0.5\textwidth]{%s}
\end{figure}
""" % image_path

    latex_content += r"\end{document}"
    return latex_content

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vuln_name = request.form["vuln_name"]
        hostname = request.form["hostname"]  
        poc = request.form["poc"]
        files = request.files.getlist("media")

        saved_files = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(filepath)
                saved_files.append(filepath)

        # Updated to use specific prompts based on user input
        vuln_desc_prompt = f"Describe vulnerability {vuln_name} for both technical and non-technical people."
        vuln_desc = query_openai(vuln_desc_prompt)
        vuln_impact = query_openai(f"What is the impact of {vuln_name}?")
        vuln_mitigation = query_openai(f"How to mitigate {vuln_name}?")

        latex_document = generate_latex_document(
            vuln_name, hostname, vuln_desc, poc, vuln_impact, vuln_mitigation, saved_files
        )

        # Save the LaTeX document
        tex_filename = os.path.join(app.config["UPLOAD_FOLDER"], "report.tex")
        with open(tex_filename, "w") as tex_file:
            tex_file.write(latex_document)

        # Compile LaTeX document to PDF
        subprocess.run(
            ["pdflatex", "-output-directory", app.config["UPLOAD_FOLDER"], tex_filename]
        )

        # Serve the PDF
        pdf_filename = tex_filename.replace(".tex", ".pdf")
        return send_from_directory(
            directory=app.config["UPLOAD_FOLDER"],
            path=os.path.basename(pdf_filename),
            as_attachment=True,
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
