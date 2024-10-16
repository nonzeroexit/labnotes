import sys
from modules import misc
from classes.Notebook import Notebook

def select_project(notebooks: list[Notebook]):
    print('ID - Project')
    for i, notebook in enumerate(notebooks):
        print(f'{i:2d} - {notebook.project}')
    while True:
        index = input('ID: ')
        if index.isdigit() and 0 <= int(index) < len(notebooks):
            return notebooks[int(index)]
        print('Wrong value, try again')

def get_args():
    if len(sys.argv) < 2 or sys.argv[1] not in ['help', 'add', 'read', 'readall', 'search'] or sys.argv[1] == 'help':
        misc.help()

    option = sys.argv[1]
    return option

def get_search_query():
    if len(sys.argv) < 3:
        sys.exit('usage:\n  labnotes search query')

    query = sys.argv[2]
    if len(query) < 2:
        sys.exit('Search query must be at least 2 characters long')
    return query

def get_n_notes():
    if len(sys.argv) < 3: # default value
        option = sys.argv[1]
        if option == 'readall':
            return 7
        if option == 'read':
            return 10
    n_notes = sys.argv[2]
    if n_notes == 'all':
        return 0
    if n_notes.isdigit() and int(n_notes) >= 1:
        return int(n_notes)
    sys.exit(f'{sys.argv[2]} is not a valid number')
