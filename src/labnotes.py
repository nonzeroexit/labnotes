#!/usr/bin/python3
import os
import sys
from modules import misc
from modules import usr_input
from classes.Notebook import Notebook
from modules.print_markdown import print_notes

def main():
    projects = misc.get_projects()
    option = usr_input.get_args()

    if option == 'readall':
        n_notes = usr_input.get_n_notes()
        notebooks = [Notebook(project) for project in projects if Notebook(project).has_content]
        notebooks_content = [f'# {notebook.project}\n{notebook.get_notes(n_notes)}' for notebook in notebooks]
        print_notes(('\n').join(notebooks_content))

    elif option =='search':
        query = usr_input.get_search_query()
        notebooks = [Notebook(project) for project in projects if Notebook(project).has_content]
        hits = [notebook.search_note(query) for notebook in notebooks]
        if not any(hits):
            misc.error('No hits found', 0)
        print_notes(('\n').join(hits))

    elif option == 'read':
        n_notes = usr_input.get_n_notes()
        project = usr_input.select_project([project for project in projects if Notebook(project).has_content])
        notebook = Notebook(project)
        if not notebook.exists or not notebook.has_content:
            misc.error('Notebook not found or empty')
        print_notes(f'# {notebook.project}\n{notebook.get_notes(n_notes)}')

    elif option == 'add':
        project = usr_input.select_project(projects)
        notebook = Notebook(project)
        note = input('Note: ')
        notebook.add_note(note)

if __name__ == '__main__':
    main()
