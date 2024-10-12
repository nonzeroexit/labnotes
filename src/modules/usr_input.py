import sys
from modules import misc

def select_project(projects):

    def choose_project(projects):

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
        for i, project in enumerate(projects):
            print(f'{i:2d} - {project}')
        return projects[get_project_index(projects)]

    project = choose_project(projects)
    return project

def get_args():
    if len(sys.argv) < 2 or sys.argv[1] not in ['add', 'read', 'readall', 'search']:
        misc.error('usage:\n  labnotes [add/read/readall/search]')

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
            misc.error('n_notes must be bigger than 0')
    except ValueError:
        misc.error(f'{sys.argv[2]} is not a valid number')
    except IndexError:
        pass
    return n_notes
