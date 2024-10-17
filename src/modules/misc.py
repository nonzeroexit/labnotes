import sys
import os

def get_projects_path():
    projects_path = os.getenv('projects_path')
    if projects_path is None:
        sys.exit('projects_path env var not configured')
    return projects_path

def get_projects():
    projects_path = get_projects_path()
    projects = sorted([folder for folder in os.listdir(projects_path) if os.path.isdir(os.path.join(projects_path, folder))])
    if len(projects) == 0:
        sys.exit('No projects found')
    return projects

def help():
    print('usage:\n  labnotes add/read [n_notes=10]/readall [n_notes=7]/search query\n  [optional]\n  to read all notes use "all"')
    sys.exit(0)
