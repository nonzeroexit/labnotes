import os
from datetime import date as get_date
from modules.misc import get_projects_path

class Notebook:
    def __init__(self, project):
        self.project = project
        self.path = os.path.join(get_projects_path(), project, 'labnotes.txt')
        self.exists = os.path.isfile(self.path)

    def get_content(self):
        with open(self.path, 'r', encoding='utf-8') as fhandle:
            notebook_content = fhandle.read().strip()
            if not notebook_content:
                return ''
            return f'# {self.project}\n{notebook_content}'

    def add_note(self, note):
        date = get_date.today().strftime("%d-%m-%y")
        with open(self.path, 'a', encoding='utf-8') as fhandle:
            if date not in self.get_content():
                fhandle.write(f'### {date}\n') # more than one note from the same day
            fhandle.write(f'* {note}\n')

    def search_note(self, query):
        hits = []
        date = 'noDate'
        for line in self.get_content().split('\n'):
            if line.startswith('###'):
                date = line.strip(' #')
            if query in line:
                hits.append(f'* {self.project} ({date})  \n{line.strip(" *")}')
        return ('\n').join(hits)

    def __repr__(self):
        return self.project
