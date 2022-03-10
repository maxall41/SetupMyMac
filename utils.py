import subprocess
import os


def is_tool(name):
    """Check whether `name` is on PATH."""

    from distutils.spawn import find_executable

    return find_executable(name) is not None
def check_if_hyperlinks_supported():
    result = subprocess.run(['node', 'check_hyperlinks.js'], stdout=subprocess.PIPE)
    if "true" in result.stdout:
        return True
    else:
        return False
