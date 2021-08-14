import os
import shutil


# Install homebrew

os.system("/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'")


# Make sure cask is installed

os.system("brew tap homebrew/cask")

# Install Iterm2

os.system("brew install --cask iterm2")

# Install Oh-My-ZSH

os.system("sh -c '$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'")

# Install VS-CODE

os.system("brew install --cask visual-studio-code")

# Install VISUAL-STUDIO

os.system("brew install --cask visual-studio")

# Install BRAVE-BROWSER

os.system("brew install --cask brave-browser")

# Install UNITY

os.system("brew install --cask unity")

# Install Postman

os.system("brew install --cask postman")

# Install Arduino

os.system("brew install --cask arduino")

# Install Boop

os.system("brew install --cask boop")

# Install Terminus

os.system("brew install --cask termius")

# Install Pock

os.system("brew install --cask pock")

# Install Istat

os.system("brew install --cask istat-menus")

# Install Node

os.system("brew install node")

# Install Gitkraken

os.system("brew install --cask gitkraken")

# Install DotFiles
    
source_dir = './DotFiles'
target_dir = '~/'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

# Install preferences

source_dir = './Preferences'
target_dir = '~/Library/Preferences'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

# Install fonts
    
source_dir = './Fonts'
target_dir = '~/Library/Fonts'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

