#!/usr/bin/python3
import os
import sys
from datetime import date
from classes.Notebook import Notebook

#TODO add markdown support

def get_project(projects_path):

    def choose_from_list(list_):

        def get_list_index(list_):
            while True:
                try:
                    index = int(input('ID: '))
                except ValueError:
                    continue
                if 0 <= index < len(list_):
                    return index

        for i, item in enumerate(list_):
            print(i, item)

        return list_[get_list_index(list_)]

    projects = sorted([folder for folder in os.listdir(projects_path) if os.path.isdir(os.path.join(projects_path, folder))])
    project = choose_from_list(projects)
    return project, os.path.join(projects_path, project, 'labnotes.txt')

def main():
    projects_path = os.getenv('projects_path')
    if projects_path is None:
        print('projects_path env var not configured')
        sys.exit(1)

    if len(sys.argv) < 2 or sys.argv[1] not in ['add', 'read', 'readall']:
        print('usage:\n  labnote [add/read/readall]')
        sys.exit(1)

    projects = sorted([folder for folder in os.listdir(projects_path) if os.path.isdir(os.path.join(projects_path, folder))])
    notebooks = [Notebook(project) for project in projects]

    option = sys.argv[1]
    if option in ['read', 'readall'] and not any([notebook.exists for notebook in notebooks]):
        print('No notebooks found.')
        sys.exit(1)

    if option == 'readall':
        all_notebooks_content = ('').join([notebook.get_content() for notebook in notebooks if notebook.exists])
        print(all_notebooks_content)
        sys.exit(0)

    project, project_notes_path = get_project(projects_path)
    if option == 'read':
        print(f'\nNOTES FROM: {project}\n')
        os.system(f'cat {project_notes_path}')
        sys.exit(0)

    if option == 'add':
        note = input('Note: ')
        today = date.today()
        text_line = f'# {today.strftime("%d-%m-%y")} - {note}\n'
        with open(project_notes_path, 'a', encoding='utf-8') as notes:
            notes.write(text_line)
        print(f'Note saved on project: {project}')
        sys.exit(0)

if __name__ == '__main__':
    main()
