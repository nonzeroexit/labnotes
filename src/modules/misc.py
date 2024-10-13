import sys
import os

def get_projects_path():
    projects_path = os.getenv('projects_path')
    if projects_path is None:
        error('projects_path env var not configured')
    return projects_path

def get_projects():
    projects_path = get_projects_path()
    projects = sorted([folder for folder in os.listdir(projects_path) if os.path.isdir(os.path.join(projects_path, folder))])
    if len(projects) == 0:
        error('No projects found', 0)
    return projects

def error(msg, code = 1):
    print(msg)
    sys.exit(code)

def help():
    print('usage:\n  labnotes add/read [n_notes]/readall [n_notes]/search query\n  [optional]')
    sys.exit(0)
