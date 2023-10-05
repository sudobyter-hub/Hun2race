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

**LaTeX** is the foundation of Hun2race. It's essential for creating those stunning PDFs. If you're new to LaTeX or haven't installed it yet, don't worry! Here's a step-by-step guide tailored just for you:

### For the APT Magicians (Ubuntu/Debian) 🧙

1. **Open Terminal**: You can do this by pressing `Ctrl` + `Alt` + `T` simultaneously.
2. **Update Repositories**: It's always good to get the latest updates:
   ```bash
   sudo apt-get update
   ```
3. **Install LaTeX**: Use the following command to install the full LaTeX suite:
   ```bash
   sudo apt-get install texlive-full
   ```

### For the PACMAN Enthusiasts (Arch Linux/Manjaro) 🕹️

1. **Open Terminal**: You can do this via your application menu or launcher.
2. **Install LaTeX**: Get the most out of LaTeX with this:
   ```bash
   sudo pacman -S texlive-most
   ```

### For the MAC Admirers 🍎

1. **Open Terminal**: You can find this in `Applications/Utilities` or simply use Spotlight to search for it.
2. **Install Homebrew** (if not installed): Homebrew is a package manager for macOS. Install it using:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. **Install LaTeX**:
   ```bash
   brew install basictex
   ```

### For the WINDOWS Warriors 🪟

1. **Open Command Prompt** (CMD) or PowerShell.
2. **Install Chocolatey** (if not installed): Chocolatey is a package manager for Windows. Install it by following instructions at [Chocolatey's installation page](https://chocolatey.org/install).
3. **Install LaTeX**: Once Chocolatey is ready, use this:
   ```bash
   choco install texlive
   ```

Remember, after installing LaTeX, you might need to restart your terminal or even your computer for some changes to take effect. Now, you're all set to let Hun2race weave its magic! 🌟


## 📞 Need Help? 

Facing challenges? I'm here for you! Connect with me on Twitter 🐦: [@aliwaleedhum](https://www.twitter.com/aliwaleedhum).

## 🤝 Join the Quest!

Your insights are golden! 🌟 Reach out at `sudobyter@gmail.com` to sprinkle your magic, collaborate in our quest, or report any dragons (bugs) you might encounter! 🐉🔍






