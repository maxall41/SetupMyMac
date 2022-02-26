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
from fontTools.ttLib import TTFont

# Make sure cask is installed

os.system("brew tap homebrew/cask")

# Install XXH

os.system("brew install xxh")

# Install zoom

os.system("brew install --cask zoom")

# Install crypto

os.system("pip3 install cryptography")

# Install ITERM2

os.system("brew install --cask iterm2")

# Install OH-MY-ZSH

os.system("sh -c '$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'")

# Install VS-CODE

os.system("brew install --cask visual-studio-code")

# Install RIDER

os.system("brew install --cask rider")

# Install BRAVE-BROWSER

os.system("brew install --cask brave-browser")

# Install UNITY-HUB

os.system("brew install --cask unity-hub")

# Install FIGMA

os.system("brew install --cask figma")

# Install POSTMAN

os.system("brew install --cask postman")

# Install ARDUINO

os.system("brew install --cask arduino")

# Install BOOP

os.system("brew install --cask boop")

# Install TERMINUS

os.system("brew install --cask termius")

# Install POCK

os.system("brew install --cask pock")

# Install ISTAT-MENUS

os.system("brew install --cask istat-menus")

# Install dash

os.system("brew install --cask dash")

# Install GIT-KRAKEN

os.system("brew install --cask gitkraken")


# Extra

print("🚀 [bold green] Installed APPS[/bold green]")

# Install DOT-FILES
    
source_dir = './DotFiles'
target_dir = '~/'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

print("🚀 [bold green]Installed DOTFILES[/bold green]")

# Install FONTS
    
source_dir = './Fonts'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    font = TTFont("./Fonts/" + file_name)
    font.save()

print("🚀 [bold green]Installed FONTS[/bold green]")
# Other stuff
print("[bold purple]--------------- DONE ---------------[/bold purple]")
print("[bold yellow]Some steps must be taken manually to install the following tools:\nRoy: https://www.useroy.com\nMagnet: https://apps.apple.com/us/app/magnet/id441258766?mt=12[/bold yellow]")
