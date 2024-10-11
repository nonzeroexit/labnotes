#!/usr/bin/python3
import os
import sys
from datetime import date as get_date
from modules import usr_input
from classes.Notebook import Notebook
from modules.print_markdown import print_notes

def main():
    projects_path = os.getenv('projects_path')
    if projects_path is None:
        print('projects_path env var not configured')
        sys.exit(1)

    projects = sorted([folder for folder in os.listdir(projects_path) if os.path.isdir(os.path.join(projects_path, folder))])
    if len(projects) == 0:
        print('No projects found')
        sys.exit(0)
    option = usr_input.get_args()

    if option == 'readall':
        notebooks = [Notebook(project, projects_path) for project in projects]
        all_notebooks_content = ('\n').join([notebook.get_content() for notebook in notebooks if notebook.exists])
        print_notes(all_notebooks_content)
        sys.exit(0)

    project = usr_input.select_project(projects)
    notebook = Notebook(project, projects_path)
    if option == 'read':
        print_notes(notebook.get_content() if notebook.exists else 'Notebook not found')

    if option == 'add':
        note = input('Note: ')
        date = get_date.today().strftime("%d-%m-%y")
        notebook.add_note(note, date)

if __name__ == '__main__':
    main()
