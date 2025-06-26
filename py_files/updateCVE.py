# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 16:43:04 2025

@author: majit
"""

import subprocess
import os

repo_path = r"C:\Users\majit\Downloads\cvelistV5-main"

os.chdir(repo_path)
result = subprocess.run(["git", "pull"], capture_output=True, text=True)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)