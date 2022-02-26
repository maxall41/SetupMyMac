import os

def bootstrap():
  # Install NODE
  os.system("brew install node")
  # Install lib for checking hyperlink compat
  os.system("npm install supports-hyperlinks")

def pre_bootstrap():
  # Install RICH
  os.system("pip3 install rich")
