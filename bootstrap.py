import os

def bootstrap():
  # Install NODE
  os.system("brew install node")
def pre_bootstrap():
  # Install RICH
  os.system("pip3 install rich")
