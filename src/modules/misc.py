import sys
import os

def get_projects_path():
    projects_path = os.getenv('projects_path')
    if projects_path is None:
        print('projects_path env var not configured')
        sys.exit(1)
    return projects_path

def get_projects():
    projects_path = get_projects_path()
    projects = sorted([folder for folder in os.listdir(projects_path) if os.path.isdir(os.path.join(projects_path, folder))])
    if len(projects) == 0:
        print('No projects found')
        sys.exit(0)
    return projects
