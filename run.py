# IMPORT LIBS

import os
import shutil

# Install HOMEBREW

os.system("/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'")

# Make sure cask is installed

os.system("brew tap homebrew/cask")

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

# Install VISUAL-STUDIO

os.system("brew install --cask visual-studio")

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

# Install command line tools

os.system("xcode-select --install")

# Install dash

os.system("brew install --cask dash")

# Install GIT-KRAKEN

os.system("brew install --cask gitkraken")

# Install DOT-FILES
    
source_dir = './DotFiles'
target_dir = '~/'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

# Install PREFERENCES

source_dir = './Preferences'
target_dir = '~/Library/Preferences'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

# Install FONTS
    
source_dir = './Fonts'
target_dir = '~/Library/Fonts'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

# Install APPS

# import os
# import shutil

# try:
#     os.system("git clone git@github.com:maxall41/apps-no-redis.git")
# except:
#     print("")

# source_dir = './apps-no-redis'
# target_dir = 'C:/Users/maxcampbell/'

# file_names = os.listdir(source_dir)

# for file_name in file_names:
#     if (file_name[0] != "."):
#         shutil.unpack_archive(os.path.join(source_dir, file_name), target_dir)
