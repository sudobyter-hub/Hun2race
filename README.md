# 🛠️ Hun2race 

![Hun2race](hun2race.gif)

**Hun2race** is a cutting-edge automated report generation tool tailored for bug hunters and penetration testers. 🐜💻 Using the power of **GOOGLE BARD / CHATGPT**, it crafts swift responses, making report creation a breeze! 🌪️ And with the magic of **LaTeX**, it spins out templates, allowing you to generate sleek PDFs. 📄✨

> 🚨 **Heads up!** This tool is still in its beta phase, so tread with excitement and caution!

## 🚀 Getting Started

1. **Set Up**: Begin your journey by cloning the repository:
`git clone https://github.com/sudobyter-hub/Hun2race.git`

2. **Prep Up**: Dive into the world of Python and get all the essentials:
`pip install -r requirements.txt`


3. **Tweak**: Make it personal! Edit the `hun2race.py` to replace the API Key. If you're lost, the Google BARD-API section below is your map! 🗺️

4. **LaTeX Love**: Ensure you've got `LaTeX` installed on your machine. It's the heart of our tool! ❤️

5. **Action Time**: Unleash the power:

`python3 hun2race.py -f bug_bounty -v idor -t attacker.com -P "Insert your PoC here"`


6. **Voilà!** 🎉 Check your directory, and behold the masterpiece of a report, ready to be shown to the world!

## 🗝️ Keys to the Kingdom 

### CHATGPT Key 🔐

1. Venture into your OPENAPI account.
2. Forge a new key and guard it like treasure! 🏴‍☠️
3. Integrate its power into `hun2race.py`.

### Google BARD Key 🎶

1. Step into the mystical lands of Google BARD.
2. Authenticate your presence.
3. Extract the essence of `__Secure-1PSID` from the cookies.
4. Imbue this essence into `hun2race.py`.

## 📖 Setting Up LaTeX 

**LaTeX** is the soul of Hun2race. Ensure it's with you!

- **For the APT magicians**: 🧙

`sudo apt-get install texlive-full`


- **For the PACMAN enthusiasts**: 🕹️
`sudo pacman -S texlive-most`


- **For the MAC admirers**: 🍎
`brew install basictex`


- **For the WINDOWS warriors**: 🪟
`choco install texlive`


## 📞 Need Help? 

Facing challenges? I'm here for you! Connect with me on Twitter 🐦: [@aliwaleedhum](https://www.twitter.com/aliwaleedhum).

## 🤝 Join the Quest!

Your insights are golden! 🌟 Reach out at `sudobyter@gmail.com` to sprinkle your magic, collaborate in our quest, or report any dragons (bugs) you might encounter! 🐉🔍






