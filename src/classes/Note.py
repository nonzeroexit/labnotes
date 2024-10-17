import sys

class Note:
    def __init__(self, note, date, project = ''):
        self.note = note
        self.date = date
        self.project = project

    def get_note_w_format(self, format, include_date = False):
        assert format in ['date_note', 'project_date_note', 'markdown']
        if format == 'date_note':
            return f'* **({self.date})** {self.note}'
        if format == 'project_date_note':
            return f'* **({self.project}:{self.date})** {self.note}'
        if format == 'markdown':
            return f'# {self.date}\n* {self.note}\n' if include_date else f'* {self.note}\n'
        sys.exit(f'{format} is a wrong format')

    def __repr__(self):
        return self.note
