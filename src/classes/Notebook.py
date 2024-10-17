import os
from datetime import date as get_date
from modules.misc import get_projects_path

NO_DATE = 'NO_DATE'

class Notebook:
    def __init__(self, project):
        self.project = project
        self.path = os.path.join(get_projects_path(), project, 'labnotes.txt')
        self.has_content = os.path.isfile(self.path) and os.path.getsize(self.path) > 0

    def get_content(self):
        with open(self.path, 'r', encoding='utf-8') as fhandle:
            notebook_content = fhandle.read().strip()
            return notebook_content

    def get_notes(self, n_notes: int):
        date = NO_DATE
        lines = []
        for i, line in enumerate(self.get_content().split('\n')):
            if line.startswith('#'):
                date = line.strip(' #')
            if line.startswith('*'):
                lines.append(f'* **({date})** {line.strip(" *")}')
        return ('\n').join(lines[-n_notes:])

    def add_note(self, note: str):
        date = get_date.today().strftime("%d-%m-%y")
        with open(self.path, 'a', encoding='utf-8') as fhandle:
            if date not in self.get_content(): # first note of the day
                fhandle.write(f'### {date}\n')
            fhandle.write(f'* {note}\n')
        print(f'Note added successfully to {self.project}')

    def search_note(self, query: str):
        hits = []
        date = NO_DATE
        for line in self.get_content().split('\n'):
            if line.startswith('###'):
                date = line.strip(' #')
            if query in line:
                hits.append(f'* {self.project} ({date})  \n{line.strip(" *")}')
        return ('\n').join(hits)

    def __repr__(self):
        return self.project
