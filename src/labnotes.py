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
        notebooks = [Notebook(project) for project in projects]
        all_notebooks_content = ('\n').join([notebook.get_content() for notebook in notebooks if notebook.exists])
        print_notes(all_notebooks_content)
        sys.exit(0)

    if option == 'search':
        query = usr_input.get_search_query()
        notebooks = [Notebook(project) for project in projects]
        notebooks = [notebook for notebook in notebooks if notebook.exists]
        hits = []
        for notebook in notebooks:
            hits += notebook.search_note(query)
        if not hits:
            misc.error('No hits found', 0)
        for hit in hits:
            print_notes(hit)
        sys.exit(0)

    project = usr_input.select_project(projects)
    notebook = Notebook(project)
    if option == 'read':
        print_notes(notebook.get_content() if notebook.exists else 'Notebook not found')

    if option == 'add':
        note = input('Note: ')
        notebook.add_note(note)

if __name__ == '__main__':
    main()
