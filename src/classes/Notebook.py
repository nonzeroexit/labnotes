import os

class Notebook:
    def __init__(self, project):
        self.path = os.path.join(os.getenv('projects_path'), project, 'labnotes.txt')
