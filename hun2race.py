import requests
from urllib.parse import urlparse
import argparse
import subprocess
from bardapi import Bard
import os
import openai

# Set Bard API KEY
os.environ["_BARD_API_KEY"] = ""
# Set OpenAI API Key
openai.api_key = ''

# LaTeX Template with Dynamic Image Placeholder
BUG_BOUNTY_TEMPLATE = r"""
\documentclass{{article}}
\usepackage{{graphicx}}
\begin{{document}}
\title{{Bug Bounty Report}}
\author{{Security Researcher}}
\date{{\today}}
\maketitle
\newpage 
\section{{Summary}}
Format: Bug Bounty \\
Vulnerability Type: {vulnerability} \\
Host: {host}
\newpage 
\section{{Vulnerability Description}}
{vulnerability_desc}
\section{{Proof of Concept}}
{proof_of_concept}
\section{{Impact}}
{impact_description}
\section{{Recommendations}}
{suggestions}
\section{{Attachments}}
{image_latex}
\end{{document}}
"""


def validate_image_url(url):
    """ Validates if the URL points to an image """
    parsed = urlparse(url)
    for ext in ['.jpg', '.jpeg', '.png', '.gif']:
        if parsed.path.endswith(ext):
            return True
    return False


def download_image_from_url(url, save_path=None):
    """ Downloads an image from a URL and saves it to a specified path """
    if not validate_image_url(url):
        raise ValueError(f"URL {url} does not seem to point to a valid image.")

    response = requests.get(url, stream=True)
    response.raise_for_status()

    if not save_path:
        save_path = url.split("/")[-1]

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    return save_path


def get_description_from_bard(prompt):
    bard_response = Bard().get_answer(str(prompt))
    return bard_response.get('content')


def get_description_from_chatgpt(prompt):
    response = openai.Completion.create(model="text-davinci-002", prompt=prompt, max_tokens=2500)
    return response.choices[0].text.strip()


def generate_image_latex_code(image_paths):
    """Generates LaTeX code to embed multiple images."""
    image_latex = ""
    for path in image_paths:
        image_latex += r"\includegraphics[width=\linewidth]{" + path + "}\n\\newpage\n"
    return image_latex


def generate_latex_report(format_type, vulnerability_type, target, vulnerability_desc, proof_of_concept,
                          impact_description, suggestions, image_latex=""):
    if format_type == 'bug_bounty':
        template = BUG_BOUNTY_TEMPLATE
    else:
        raise ValueError('Invalid report format')

    report = template.format(
        vulnerability=vulnerability_type,
        host=target,
        vulnerability_desc=vulnerability_desc,
        proof_of_concept=proof_of_concept,
        impact_description=impact_description,
        suggestions=suggestions,
        image_latex=image_latex
    )
    return report


def main():
    parser = argparse.ArgumentParser(description='Security Research Report Generator')
    parser.add_argument('-f', '--format', choices=['bug_bounty', 'pentesting'], required=True, help='Report format')
    parser.add_argument('-v', '--vulnerability', required=True, help='Type of vulnerability')
    parser.add_argument('-t', '--target', required=True, help='Host where the vulnerability was found')
    parser.add_argument('-P', '--poc', required=True, help='PoC of the bug')
    parser.add_argument('-e', '--engine', choices=['bard', 'chatgpt'], required=True,
                        help='Choice of description engine')
    parser.add_argument('-i', '--images', nargs='*', help='URLs of the images to include in the report', default=[])

    args = parser.parse_args()

    # Generate the prompts
    vulnerability_desc_prompt = f"describe the following bug {args.vulnerability} with details to technical and non technical people"
    impact_description_prompt = f"what is the impact of this {args.vulnerability} and how it might affect the company"
    suggestions_prompt = f"what do you suggest to fix this {args.vulnerability} write full details"

    # Use either bard or chatgpt based on the user's choice
    if args.engine == 'bard':
        vulnerability_desc = get_description_from_bard(vulnerability_desc_prompt)
        impact_description = get_description_from_bard(impact_description_prompt)
        suggestions = get_description_from_bard(suggestions_prompt)
    elif args.engine == 'chatgpt':
        vulnerability_desc = get_description_from_chatgpt(vulnerability_desc_prompt)
        impact_description = get_description_from_chatgpt(impact_description_prompt)
        suggestions = get_description_from_chatgpt(suggestions_prompt)

    image_paths = []
    for img_url in args.images:
        try:
            image_path = download_image_from_url(img_url)
            image_paths.append(image_path)
            print(f"Image downloaded from {img_url} and saved as {image_path}")
        except Exception as e:
            print(f"Error downloading image from {img_url}: {e}")
            return

    if not image_paths:
        print("No valid images provided. The Attachments section will not be included.")
    else:
        image_latex_code = generate_image_latex_code(image_paths)

    latex_report = generate_latex_report(args.format, args.vulnerability, args.target, vulnerability_desc, args.poc,
                                         impact_description, suggestions, image_latex=image_latex_code)

    with open('security_report.tex', 'w') as f:
        f.write(latex_report)

    print("LaTeX report generated successfully.")

    # Compile LaTeX report to PDF and display any errors
    try:
        result = subprocess.run(['pdflatex', "security_report.tex"], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error occurred while compiling LaTeX to PDF.")
            print(result.stderr)
        else:
            print("PDF report generated successfully.")
    except Exception as e:
        print(f"Error during LaTeX compilation: {e}")


if __name__ == '__main__':
    main()
