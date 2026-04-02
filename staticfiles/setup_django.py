import os
import subprocess

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

try:
    python_bin = "./venv/bin/python"
    
    # 1. Initialize the core project
    if not os.path.exists("manage.py"):
        run(f"{python_bin} -m django startproject pejuni_config .")
    else:
        print("Project already cleanly initialized.")

    # 2. Build the apps
    apps = ["core", "services", "projects", "team", "news"]
    for app in apps:
        if not os.path.exists(app):
            run(f"{python_bin} manage.py startapp {app}")
            print(f"Created app: {app}")
        else:
            print(f"App {app} already exists.")
            
    print("SUCCESS! All Django components perfectly initialized.")

except Exception as e:
    print(f"ERROR: {e}")
