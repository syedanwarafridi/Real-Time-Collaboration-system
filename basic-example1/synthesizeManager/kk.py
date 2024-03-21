# Updated SynthesisManager.py

import nbformat
from nbformat.v4 import new_markdown_cell
from nbformat import write

class SynthesisManager:
    def __init__(self):
        self.sections = []
        self.resources = []

    def create_and_add_section_then_return_id(self, notebook_path, title):
        section_id = len(self.sections) + 1
        self.sections.append({"id": section_id, "title": title})

        # Load the notebook
        with open(notebook_path, 'r') as f:
            notebook = nbformat.read(f, as_version=4)

        # Create a new Markdown cell with the section content
        section_content = f"# Synth {section_id}\n\nThis is the content of Section {section_id}."
        new_cell = new_markdown_cell(section_content)

        # Add the new cell to the notebook
        notebook['cells'].append(new_cell)

        # Save the modified notebook
        with open(notebook_path, 'w') as f:
            write(notebook, f)

        return section_id
