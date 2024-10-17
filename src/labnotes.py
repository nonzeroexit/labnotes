#!/usr/bin/python3
import os
import sys
from modules import misc
from modules import usr_input
from modules.print_markdown import print_notes

def main():
    projects = misc.get_projects()
    option = usr_input.get_args()
    notebooks, notebooks_w_content = misc.get_notebooks(projects, option)

    if option == 'read':
        n_notes = usr_input.get_n_notes()
        notebook = usr_input.select_project(notebooks_w_content)
        print_notes(f'# {notebook.project}\n{notebook.get_notes(n_notes)}')

    elif option == 'readall':
        n_notes = usr_input.get_n_notes()
        notebooks_content = [f'# {notebook.project}\n{notebook.get_notes(n_notes)}' for notebook in notebooks_w_content]
        print_notes(('\n').join(notebooks_content))

    elif option =='search':
        query = usr_input.get_search_query()
        hits = [notebook.search_note(query) for notebook in notebooks_w_content]
        if not any(hits):
            sys.exit('No hits found')
        print_notes(('\n').join(hits))

    elif option == 'add':
        notebook = usr_input.select_project(notebooks)
        note = input('Note: ')
        notebook.add_note(note)

if __name__ == '__main__':
    main()
