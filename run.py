# IMPORT LIBS

import os
import shutil
import subprocess
import bootstrap
import utils

# Run pre bootstrap setup code

bootstrap.pre_bootstrap()

# Check if Homebrew is installed

if utils.is_tool("brew") == False:
    print("[bold red]Please install [link=https://brew.sh]Homebrew[/link] then run this script again[/bold red] 🍺")
    print("Link: https://brew.sh")
    exit()

# Run bootstrap

bootstrap.bootstrap()

# Import stuff after bootstrap

from rich import print

# Make sure cask is installed

os.system("brew tap homebrew/cask")

# Install UnRar

os.system("brew install unar")

# Install Poetry

os.system("curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -")

# Install Oh My ZSH

os.system("sh -c '$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'")

# Install Powerlevel10K

os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k")

# Install XXH

os.system("brew install xxh")

# Install zoom

os.system("brew install --cask zoom")

# Install crypto

os.system("pip3 install cryptography")

# Install BAT

os.system("brew install bat")

# Install ITERM2

os.system("brew install --cask iterm2")

# Install Mosh

os.system("brew install mosh")

# Install OH-MY-ZSH

os.system("sh -c '$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'")

# Install VS-CODE

os.system("brew install --cask visual-studio-code")

# Install RIDER

os.system("brew install --cask rider")

# Install BRAVE-BROWSER

os.system("brew install --cask brave-browser")

# Install BOTTOm

os.system("brew install bottom")

# Install UNITY-HUB

os.system("brew install --cask unity-hub")

# Install FIGMA

os.system("brew install --cask figma")

# Install POSTMAN

os.system("brew install --cask postman")

# Install MICRO

os.system("brew install micro")

# Install GeforceNow

os.system("brew install --cask nvidia-geforce-now")

# Install ARDUINO

os.system("brew install --cask arduino")

# Install BOOP

os.system("brew install --cask boop")

# Install FIG

os.system("brew install --cask fig")

# Install TERMINUS

os.system("brew install --cask termius")

# Install STEAM

os.system("brew install --cask steam")

# Install Balena

os.system("brew install --cask balenaetcher")

# Install EXA

os.system("brew install exa")

# Install raspberry pi imager

os.system("brew install --cask raspberry-pi-imager")

# Install thefuck

os.system("brew install thefuck")

# Install golang

os.system("brew install go")

# Install image tools

os.system("brew install imagemagick")

# Install Archey

os.system("brew install archey")

# Install NVM

os.system("brew install nvm")

# Install WGET

os.system("brew install wget")

# Install dash

os.system("brew install --cask dash")

# Install Teams

os.system("brew install --cask microsoft-teams")

# Install GIT-KRAKEN

os.system("brew install --cask gitkraken")

# Install Yarn

os.system("npm install --global yarn")

# Install MORO

os.system("yarn global add moro")

# Extra

print("🚀 [bold green] Installed APPS[/bold green]")

# Install Aliases
    
source_file = './aliases.zsh'
target_dir = '../../.oh-my-zsh/custom/aliases.zsh'

shutil.copy(source_file, target_file)

print("🚀 [bold green]Installed Aliases[/bold green]")

# Install DOT-FILES
    
source_dir = './DotFiles'
target_dir = '../../'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.copy(os.path.join(source_dir, file_name), target_dir)

print("🚀 [bold green]Installed DOTFILES[/bold green]")

# Install FONTS
    
source_dir = './Fonts'
target_dir = '../../Library/Fonts'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.copy(os.path.join(source_dir, file_name), target_dir)

print("🚀 [bold green]Installed FONTS[/bold green]")

# Other stuff
print("[bold purple]--------------- DONE ---------------[/bold purple]")
print("[bold yellow]Some steps must be taken manually to install the following tools:\nRoy: https://www.useroy.com\nMagnet: https://apps.apple.com/us/app/magnet/id441258766?mt=12\nIterm2 theme[/bold yellow]")
