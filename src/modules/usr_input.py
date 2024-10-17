import sys
from modules import misc

def select_project(projects: list[str]):
    if len(projects) == 1:
        return projects[0]
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
        sys.exit('usage:\n  labnotes search query')

    query = sys.argv[2]
    if len(query) < 2:
        sys.exit('Search query must be at least 2 characters long')
    return query

def get_n_notes():
    if len(sys.argv) < 3:
        return 0 # all notes
    if sys.argv[2].isdigit() and int(sys.argv[2]) > 0:
        return int(sys.argv[2])
    sys.exit(f'{sys.argv[2]} is not a valid number')
