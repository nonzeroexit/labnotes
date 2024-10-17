import os
from classes.Note import Note
from datetime import date as get_date

NO_DATE = 'NO_DATE'

class Notebook:
    def __init__(self, project):
        self.project = project
        self.path = os.path.join(project, 'labnotes.md')
        self.has_content = os.path.isfile(self.path) and os.path.getsize(self.path) > 0

    def _get_content(self):
        assert self.has_content
        with open(self.path, 'r', encoding='utf-8') as fhandle:
            notebook_content = fhandle.read().strip()
            return notebook_content

    def _get_all_notes(self):
        date = NO_DATE
        notes = []
        for line in self._get_content().split('\n'):
            if line.startswith('#'):
                date = line.strip(' #')
            elif line.startswith('*'):
                note = Note(line.strip(' *'), date, self.project)
                notes.append(note)
        return notes

    def get_notes(self, n_notes: int):
        notes = [note.get_note_w_format('date_note') for note in self._get_all_notes()[-n_notes:]]
        return ('\n').join(notes)

    def add_note(self, note: str):
        new_note = Note(note, get_date.today().strftime("%d-%m-%y"))
        include_date = not self.has_content or new_note.date not in self._get_content() # empty notebook or first note of the day
        with open(self.path, 'a', encoding='utf-8') as fhandle:
            fhandle.write(new_note.get_note_w_format('markdown', include_date))
        print(f'Note added successfully to {self.project}')

    def search_note(self, query: str):
        hits = [note.get_note_w_format('project_date_note') for note in self._get_all_notes() if query in note.note or query in note.date]
        return ('\n').join(hits)

    def __repr__(self):
        return self.project
