import argparse
import subprocess
from bardapi import Bard
import os
import openai  

# Bard API KEY
os.environ["_BARD_API_KEY"] = "Your Bard API Key"
# Set OpenAI API Key
openai.api_key = 'Your OPENAI API KEY'

# ASCII Art & Help Text
print('''
▒█░▒█ ▒█░▒█ ▒█▄░▒█ █▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▀ 
▒█▀▀█ ▒█░▒█ ▒█▒█▒█ ░▄▀ ▒█▄▄▀ ▒█▄▄█ ▒█░░░ ▒█▀▀▀ 
▒█░▒█ ░▀▄▄▀ ▒█░░▀█ █▄▄ ▒█░▒█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄
By : sudobyter 
Usage : 
        -f , report format (bugbounty, pentesting)
        -v , vulnerability type 
        -t , target site 
        -P , PoC of the bug
        -e , choice of description engine (bard or chatgpt)
        example : 
        python3 hun2race.py -f bugbounty -v IDOR -t attacker.com -P "Found IDOR on the following domain etc..." -e bard/chatgpt
      ''')

# LaTeX Template
BUG_BOUNTY_TEMPLATE = r"""
\documentclass{{article}}
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
\end{{document}}
"""

def get_description_from_bard(prompt):
    bard_response = Bard().get_answer(str(prompt))
    return bard_response.get('content')

def get_description_from_chatgpt(prompt):
    response = openai.Completion.create(model="text-davinci-002", prompt=prompt, max_tokens=500)
    return response.choices[0].text.strip()

def generate_latex_report(format_type, vulnerability_type, target, vulnerability_desc, proof_of_concept, impact_description, suggestions):
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
        suggestions=suggestions
    )
    return report

def main():
    parser = argparse.ArgumentParser(description='Security Research Report Generator')
    parser.add_argument('-f', '--format', choices=['bug_bounty', 'pentesting'], required=True, help='Report format')
    parser.add_argument('-v', '--vulnerability', required=True, help='Type of vulnerability')
    parser.add_argument('-t', '--target', required=True, help='Host where the vulnerability was found')
    parser.add_argument('-P', '--poc', required=True, help='PoC of the bug')
    parser.add_argument('-e', '--engine', choices=['bard', 'chatgpt'], required=True, help='Choice of description engine')
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

    latex_report = generate_latex_report(args.format, args.vulnerability, args.target, vulnerability_desc, args.poc, impact_description, suggestions)

    # Save the LaTeX report to a .tex file
    with open('security_report.tex', 'w') as f:
        f.write(latex_report)

    print("LaTeX report generated successfully.")

    # Compile LaTeX report into PDF
    try:
        subprocess.run(['pdflatex', "security_report.tex"])
        print("YAY! PDF report generated successfully.")
    except subprocess.CalledProcessError:
        print("Error occurred while compiling LaTeX to PDF.")

if __name__ == '__main__':
    main()
