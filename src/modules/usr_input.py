def select_project_notebook(notebooks):

    def choose_project(notebooks):

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
        for i, notebook in enumerate(notebooks):
            print(f'{i:2d} - {notebook.project}')
        return notebooks[get_project_index(notebooks)]

    notebook = choose_project(notebooks)
    return notebook
