import os
from datetime import date as get_date

NO_DATE = 'NO_DATE'

class Notebook:
    def __init__(self, project):
        self.project = project
        self.path = os.path.join(project, 'labnotes.md')
        self.has_content = os.path.isfile(self.path) and os.path.getsize(self.path) > 0

    def _get_content(self):
        with open(self.path, 'r', encoding='utf-8') as fhandle:
            notebook_content = fhandle.read().strip()
            return notebook_content

    def get_notes(self, n_notes: int):
        date = NO_DATE
        notes = []
        for line in self._get_content().split('\n'):
            if line.startswith('#'):
                date = line.strip(' #')
            elif line.startswith('*'):
                notes.append(f'* **({date})** {line.strip(" *")}')
        return ('\n').join(notes[-n_notes:])

    def add_note(self, note: str):
        date = get_date.today().strftime("%d-%m-%y")
        with open(self.path, 'a', encoding='utf-8') as fhandle:
            if date not in self._get_content(): # first note of the day
                fhandle.write(f'# {date}\n')
            fhandle.write(f'* {note}\n')
        print(f'Note added successfully to {self.project}')

    def search_note(self, query: str):
        date = NO_DATE
        hits = []
        for line in self._get_content().split('\n'):
            if line.startswith('#'):
                date = line.strip(' #')
            if query in line:
                hits.append(f'* **({self.project}:{date})** {line.strip(" *")}')
        return ('\n').join(hits)

    def __repr__(self):
        return self.project
