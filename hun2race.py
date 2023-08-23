import argparse
import subprocess
import openai
from bardapi import Bard
import os
import requests

# Bard API KEY
os.environ["_BARD_API_KEY"] = "INSERT YOU BARD KEY (__Secure-1PSID)"


print('''



▒█░▒█ ▒█░▒█ ▒█▄░▒█ █▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▀ 
▒█▀▀█ ▒█░▒█ ▒█▒█▒█ ░▄▀ ▒█▄▄▀ ▒█▄▄█ ▒█░░░ ▒█▀▀▀ 
▒█░▒█ ░▀▄▄▀ ▒█░░▀█ █▄▄ ▒█░▒█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄


By : sudobyter 

Usage : 
        -f , report format (bugbounty, pentesting)
        -v , vulnerability type 
        -t , target site 
        
        example : 
        python3 hun2race.py -f bugbounty -v IDOR -t attacker.com -P "Found IDOR on the following domain etc..." 

      ''')



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
    parser.add_argument('-f', '--format', choices=['bug_bounty', 'pentesting'], required=True, help='Report format (bug_bounty or pentesting)')
    parser.add_argument('-v', '--vulnerability', required=True, help='Type of vulnerability')
    parser.add_argument('-t', '--target', required=True, help='Host where the vulnerability was found')
    parser.add_argument('-P', '--poc', required=True, help='PoC of the bug')

    args = parser.parse_args()

    vulnerability_type = args.vulnerability
    target = args.target
    proof_of_concept = args.poc

    print(f"Generating {args.format} report for {vulnerability_type} on {target}...")

    vulnerability_desc = f"describe the following bug {vulnerability_type} with details to technical and non technical people"
    impact_description = f"what is the impact of this {vulnerability_type} and how it might effect the company"
    suggestions = f"what do you suggest to fix this {vulnerability_type} write full details"

    # Set the path where you want to save the downloaded image


    bard_vuln_desc = Bard().get_answer(str(vulnerability_desc))

    response_bard_vuln_desc = bard_vuln_desc.get('content')

    bard_impact_desc = Bard().get_answer(str(impact_description))

    response_bard_impact_desc = bard_impact_desc.get('content')

    bard_suggestions = Bard().get_answer(str(suggestions))

    response_bard_suggestions = bard_suggestions.get('content')

    latex_report = generate_latex_report(args.format, vulnerability_type, target, response_bard_vuln_desc, proof_of_concept, response_bard_impact_desc, response_bard_suggestions)

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
