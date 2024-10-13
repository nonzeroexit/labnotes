import sys
from modules import misc

def select_project(projects):
    print('ID - Project')
    for i, project in enumerate(projects):
        print(f'{i:2d} - {project}')
    while True:
        index = input('ID: ')
        if index.isdigit() and 0 <= int(index) < len(projects):
            return projects[int(index)]
        else:
            print('Wrong value, try again')

def get_args():
    if len(sys.argv) < 2 or sys.argv[1] not in ['help', 'add', 'read', 'readall', 'search'] or sys.argv[1] == 'help':
        misc.help()

    option = sys.argv[1]
    return option

def get_search_query():
    if len(sys.argv) < 3:
        misc.error('usage:\n  labnotes search query')

    query = sys.argv[2]

    if len(query) < 2:
        misc.error('Search query must be at least 2 characters long')
    return query

def get_n_notes():
    n_notes = -1 # all notes
    try:
        n_notes = int(sys.argv[2])
        if n_notes < 1:
            misc.error('last_n_notes must be bigger than 0')
    except ValueError:
        misc.error(f'{sys.argv[2]} is not a valid number')
    except IndexError:
        pass
    return n_notes
