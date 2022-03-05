# IMPORT LIBS

import os
import shutil
import subprocess
import bootstrap
import utils

# Modules

def nas_module():
    try:
        confirm = Prompt.ask("[bold green]Would you like to configure a NAS? Note: This is required for downloading custom apps. y/n:[/bold green]")
        if lower(confirm) == "y":
            ip = Prompt.ask("IP: ")
            username = Prompt.ask("Username: ")
            password = Prompt.ask("Password: ")
            pool = Prompt.ask("Pool name (default: Main):",default="Main")
            os.system("open 'smb://" + username + ":" + password + "@" + ip + "/" + pool + "/" + username + "/'")
            copy_path = "../../../Volumes/" + username + "/Utils/apps"
            print("C " + copy_path)

            target_dir = './'

            file_names = os.listdir(copy_path)
            for file_name in file_names:
                shutil.copy(os.path.join(copy_path, file_name), target_dir)
                if ".dmg" in file_name:
                    os.system("hdiutil attach " + file_name)
                    app_path = "../../../Volumes/" + file_name.split(" ")[0] + "/" + file_name.split(" ")[0] + ".app"
                    os.system("cp -r " + app_path + " ../Applications/" + file_name.split(" ")[0])
                else:
                    print("[bold yellow]Not installing " + file_name + " because it has an unsupported file extension. The supported file extensions are:\n.dmg[/bold yellow]")
        else:
            print("[bold yellow]Not configuring NAS[/bold yellow]")
    except:
        print("[bold red]Failed to setup NAS...[/bold red]")
def dot_files():
    try:
        confirm = Prompt.ask("[bold green]Would you like to install apps? y/n:[/bold green]")
        if lower(confirm) == "y":
            source_dir = './DotFiles'
            target_dir = '../../'
            file_names = os.listdir(source_dir)
            for file_name in file_names:
                shutil.copy(os.path.join(source_dir, file_name), target_dir)
            print("🚀 [bold green]Installed DOTFILES[/bold green]")
        else:
            print("[bold yellow]Not installing Dotfiles[/bold yellow]")
    except:
        print("😥 [bold red]Failed to install DOTFILES[/bold red]")
def aliases():
    try:
        confirm = Prompt.ask("[bold green]Would you like to install apps? y/n:[/bold green]")
        if lower(confirm) == "y":
            source_file = './aliases.zsh'
            target_dir = '../../.oh-my-zsh/custom/aliases.zsh'

            shutil.copy(source_file, target_file)

            print("🚀 [bold green]Installed Aliases[/bold green]")
        else:
            print("[bold yellow]Not installing Aliases[/bold yellow]")
    except:
        print("😥 [bold red]Failed to install Aliases[/bold red]")
def font():
    try:
        confirm = Prompt.ask("[bold green]Would you like to install apps? y/n:[/bold green]")
        if lower(confirm) == "y":
            source_dir = './Fonts'
            target_dir = '../../Library/Fonts'

            file_names = os.listdir(source_dir)

            for file_name in file_names:
                shutil.copy(os.path.join(source_dir, file_name), target_dir)

            print("🚀 [bold green]Installed FONTS[/bold green]")
        else:
            print("[bold yellow]Not installing Fonts[/bold yellow]")
    except:
        print("😥 [bold red]Failed to install Fonts[/bold red]")

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
from rich.prompt import Prompt

# Show hidden files

os.system("defaults write com.apple.Finder AppleShowAllFiles true")

# Restart finder

os.system("killall Finder") 

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

# Install Fusion360

os.system("brew install --cask autodesk-fusion360")

# Install crypto

os.system("pip3 install cryptography")

# Install GIMP

os.system("brew install --cask gimp")

# Install BAT

os.system("brew install bat")

# Install KiCad

os.system("brew install --cask kicad")

# Install ITERM2

os.system("brew install --cask iterm2")

os.system("cp ./com.googlecode.iterm2.plist ~/Library/Preferences")

# Install Mosh

os.system("brew install mosh")

# Install OH-MY-ZSH

os.system("sh -c '$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'")

# Install Unarchiver

os.system("brew install --cask the-unarchiver")

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

# Install MAS

os.system("brew install mas")

# Use MAS to install apps

os.system("mas install 441258766") # Install Magnet

os.system("mas install 993487541") # Install Carrot Weather

# Install MICRO

os.system("brew install micro")

# Install GeforceNow

os.system("brew install --cask nvidia-geforce-now")

# Install ARDUINO

os.system("brew install --cask arduino")

# Install BOOP

os.system("brew install --cask boop")

# Install Whatsapp

os.system("brew install --cask whatsapp")

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

# Install Roy

os.system("hdiutil attach downloaded_roy_install.dmg")

# Install MORO

os.system("yarn global add moro")

# NAS Stuff

nas_module()

# Extra

print("🚀 [bold green] Installed APPS[/bold green]")

# Install Aliases
    
aliases()

# Install DOT-FILES
    
dot_files()

# Install FONTS
    
font()

# Other stuff
print("[bold purple]--------------- DONE ---------------[/bold purple]")
print("[bold yellow]Some steps must be taken manually to install the following tools:\nRoy: https://www.useroy.com\nMagnet: https://apps.apple.com/us/app/magnet/id441258766?mt=12[/bold yellow]")
