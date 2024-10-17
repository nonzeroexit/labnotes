import sys
from modules import misc
from classes.Notebook import Notebook

def select_project(notebooks: list[Notebook]):
    if len(notebooks) == 1:
        return notebooks[0]
    print('ID - Project')
    for i, notebook in enumerate(notebooks):
        print(f'{i:2d} - {notebook.project}')
    while True:
        index = input('ID: ')
        if index.isdigit() and 0 <= int(index) < len(notebooks):
            return notebooks[int(index)]
        else:
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
        match option:
            case 'readall':
                return 7
            case 'read':
                return 10
    if sys.argv[2] == 'all':
        return 0
    if sys.argv[2].isdigit() and int(sys.argv[2]) >= 1:
        return int(sys.argv[2])
    sys.exit(f'{sys.argv[2]} is not a valid number')
