import os

class Notebook:
    def __init__(self, project):
        self.project = project
        self.path = os.path.join(os.getenv('projects_path'), project, 'labnotes.txt')
        self.exists = os.path.isfile(self.path)

    def __repr__(self):
        return self.project
