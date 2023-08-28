# Hun2race
![](hun2race.gif)
Hun2race is an automated report generation tool designed for bug hunters and penetration testers. The tool utilizes GOOGLE BARD / CHATGPT to produce responses, accelerating report creation. Additionally, it leverages LaTeX to create templates, enabling the generation of PDFs.

Note: This tool is currently in its beta version.

# Guide

- Clone the repo: `git clone https://github.com/sudobyter-hub/Hun2race.git`
- Install Python requirements: `pip install -r requirements.txt`
- Edit the` hun2race.py `file to replace the API Key. For guidance, refer to the Google BARD-API section.
- Ensure `LaTeX` is installed on your machine.
- Execute the tool: `python3 hun2race.py -f bug_bounty -v idor -t attacker.com -P "Insert your PoC here"`
- Upon completion, you'll find the report, ready to be submitted, in your directory.


# CHATGPT key 
1. Access your OPENAPI account
2. Create New key (save the key in safe place)
3. Copy and replace the key in the following file `hun2race.py` 


# Google BARD key

1. Access Google BARD.
2. Sign in to your account.
3. View cookies and copy the value of `__Secure-1PSID`.
4. Insert this value into `hun2race.py`.

# LaTeX

LaTeX must be installed on your machine for this tool to work.

## APT

Run: `$ sudo apt-get install texlive-full`

## PACMAN

Run: `$ sudo pacman -S texlive-most`

## MAC

Run: `$ brew install basictex`

## WINDOWS

Run: `$ choco install texlive`

# Support 

If you are having any issues you may contact me on Twitter : [@aliwaleedhum](https://www.twitter.com/aliwaleedhum) 

# Contributions

Feel free to reach out at `sudobyter@gmail.com` for suggestions, development collaborations, or to report any issues.
