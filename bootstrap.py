import os

def bootstrap():
  # Install NODE
  os.system("brew install node")
  # Install lib for checking hyperlink compat
  os.system("npm install supports-hyperlinks")

def pre_bootstrap():
  # Make sure PIP is latest
  os.system("pip3 install --upgrade pip3")
  # Install RICH
  os.system("pip3 install rich")
