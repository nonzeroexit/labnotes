#!/usr/bin/python3
import os
import sys
from datetime import date as get_date
from classes.Notebook import Notebook

#TODO add markdown support

def select_project_notebook(notebooks):

    def choose_project(notebooks):

        def get_project_index(list_):
            while True:
                try:
                    index = int(input('ID: '))
                except ValueError:
                    print('Wrong value, try again')
                    continue
                if 0 <= index < len(list_):
                    return index
                else:
                    print('Wrong value, try again')

        print('ID - Project')
        for i, notebook in enumerate(notebooks):
            print(f'{i:2d} - {notebook.project}')
        return notebooks[get_project_index(notebooks)]

    notebook = choose_project(notebooks)
    return notebook

def main():
    projects_path = os.getenv('projects_path')
    if projects_path is None:
        print('projects_path env var not configured')
        sys.exit(1)

    if len(sys.argv) < 2 or sys.argv[1] not in ['add', 'read', 'readall']:
        print('usage:\n  labnote [add/read/readall]')
        sys.exit(1)

    projects = sorted([folder for folder in os.listdir(projects_path) if os.path.isdir(os.path.join(projects_path, folder))])
    if len(projects) == 0:
        print('No projects found')
        sys.exit(0)
    notebooks = [Notebook(project) for project in projects]

    option = sys.argv[1]
    if option in ['read', 'readall'] and not any([notebook.exists for notebook in notebooks]):
        print('No notebooks found.')
        sys.exit(1)

    if option == 'readall':
        all_notebooks_content = ('\n').join([notebook.get_content() for notebook in notebooks if notebook.exists])
        print(all_notebooks_content)
        sys.exit(0)

    notebook = select_project_notebook(notebooks)
    if option == 'read':
        print(notebook.get_content() if notebook.exists else 'Notebook not found')

    if option == 'add':
        note = input('Note: ')
        date = get_date.today().strftime("%d-%m-%y")
        notebook.add_note(note, date)

if __name__ == '__main__':
    main()
