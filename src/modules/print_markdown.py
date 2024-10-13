from rich.console import Console
from rich.markdown import Markdown

def print_notes(notes: str):
    notes_markdown = Markdown(notes)
    console = Console()
    console.print(notes_markdown)
