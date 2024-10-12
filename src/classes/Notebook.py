import os
from modules.misc import get_projects_path

class Notebook:
    def __init__(self, project):
        self.project = project
        self.path = os.path.join(get_projects_path(), project, 'labnotes.txt')
        self.exists = os.path.isfile(self.path)

    def get_content(self):
        with open(self.path, 'r', encoding='utf-8') as fhandle:
            return f'# {self.project}\n{fhandle.read().strip()}'

    def add_note(self, note, date):
        with open(self.path, 'a', encoding='utf-8') as fhandle:
            if date not in self.get_content():
                fhandle.write(f'### {date}\n') # more than one note from the same day
            fhandle.write(f'* {note}\n')

    def __repr__(self):
        return self.project
