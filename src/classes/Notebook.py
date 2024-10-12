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

    def get_last_n_notes(self, n_notes):
        n = 0
        lines = []
        reverse_content = self.get_content().split('\n')[::-1]
        for i, line in enumerate(reverse_content):
            if line.startswith('*'):
                n += 1
            lines.insert(0, line)
            if n == n_notes:
                oldest_date = [line for pos, line in enumerate(reverse_content) if pos > i and line.startswith('###') ]
                lines.insert(0, oldest_date[0] if len(oldest_date) >= 1 else 'noDate')
                break
        notes = ('\n').join(lines)
        return f'# {self.project}\n{notes}'

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
