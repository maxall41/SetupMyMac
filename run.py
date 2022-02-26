# IMPORT LIBS

import os
import shutil
import subprocess
import bootstrap

# Functions

def is_tool(name):
    """Check whether `name` is on PATH."""

    from distutils.spawn import find_executable

    return find_executable(name) is not None

# Bootstrap

bootstrap.run()

# Import stuff after bootstrap

from rich.console import Console

# Install HOMEBREW

os.system("/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'")

if is_tool("brew") == False:
    print("Please add Homebrew to your path and then run this script again 🍺")

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

# Install NODE

os.system("brew install node")

# Install dash

os.system("brew install --cask dash")

# Install GIT-KRAKEN

os.system("brew install --cask gitkraken")

print("🚀 Installed APPS")

# Install DOT-FILES
    
source_dir = './DotFiles'
target_dir = '~/'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)
print("🚀 Installed Dot files")

# Install FONTS
    
source_dir = './Fonts'
target_dir = '~/Library/Fonts'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)
print("🚀 Installed FONTS")
 # Other stuff
print("--------------- DONE ---------------")
print("Some steps must be taken manually to install the following tools:")
print("Roy")
print("Mirror")
