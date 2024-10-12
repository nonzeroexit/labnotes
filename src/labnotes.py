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
        notebooks = [Notebook(project) for project in projects if Notebook(project).exists]
        notebooks_content = [notebook.get_last_n_notes(5) for notebook in notebooks]
        print_notes(('\n').join(notebooks_content))

    elif option =='search':
        query = usr_input.get_search_query()
        notebooks = [Notebook(project) for project in projects if Notebook(project).exists]
        hits = [notebook.search_note(query) for notebook in notebooks]
        if not any(hits):
            misc.error('No hits found', 0)
        print_notes(('\n').join(hits))

    elif option == 'read':
        project = usr_input.select_project(projects)
        notebook = Notebook(project)
        print_notes(notebook.get_content() if notebook.exists else 'Notebook not found')

    elif option == 'add':
        project = usr_input.select_project(projects)
        notebook = Notebook(project)
        note = input('Note: ')
        notebook.add_note(note)

if __name__ == '__main__':
    main()
