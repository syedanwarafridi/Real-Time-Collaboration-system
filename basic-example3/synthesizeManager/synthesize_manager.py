# # SynthesisManager.py

# class SynthesisManager:
#     def __init__(self):
#         self.sections = []
#         self.resources = []

#     def create_and_add_section_then_return_id(self, title):
#         section_id = len(self.sections) + 1
#         self.sections.append({"id": section_id, "title": title})
#         return section_id

#     def edit_section(self, section_id, new_title):
#         for section in self.sections:
#             if section["id"] == section_id:
#                 section["title"] = new_title

#     def remove_section(self, section_id):
#         self.sections = [section for section in self.sections if section["id"] != section_id]

#     def swap_sections(self, section_id_1, section_id_2):
#         # Simplified swap logic for illustration
#         for section in self.sections:
#             if section["id"] == section_id_1:
#                 section["id"] = section_id_2
#             elif section["id"] == section_id_2:
#                 section["id"] = section_id_1

#     def add_resource(self, content):
#         resource_id = len(self.resources) + 1
#         self.resources.append({"id": resource_id, "content": content})
#         return resource_id

#     def edit_resource(self, resource_id, new_content):
#         for resource in self.resources:
#             if resource["id"] == resource_id:
#                 resource["content"] = new_content

#     def remove_resource(self, resource_id):
#         self.resources = [resource for resource in self.resources if resource["id"] != resource_id]

#     def swap_resources(self, resource_id_1, resource_id_2):
#         # Simplified swap logic for illustration
#         for resource in self.resources:
#             if resource["id"] == resource_id_1:
#                 resource["id"] = resource_id_2
#             elif resource["id"] == resource_id_2:
#                 resource["id"] = resource_id_1


# Updated SynthesisManager.py

import nbformat
from nbformat.v4 import new_markdown_cell, new_code_cell
from nbformat import write

class SynthesisManager:
    def __init__(self):
        self.sections = []
        self.resources = []

    def load_notebook(self, notebook_path):
        with open(notebook_path, 'r') as f:
            return nbformat.read(f, as_version=4)

    def save_notebook(self, notebook, notebook_path):
        with open(notebook_path, 'w') as f:
            write(notebook, f)

    def create_and_add_section_then_return_id(self, notebook_path, title):
        section_id = len(self.sections) + 1
        self.sections.append({"id": section_id, "title": title})

        # Load the notebook
        notebook = self.load_notebook(notebook_path)

        # Create a new Markdown cell with the section content
        section_content = f"# Section {section_id}\n\nThis is the content of Section {section_id}."
        new_cell = new_markdown_cell(section_content)

        # Add the new cell to the notebook
        notebook['cells'].append(new_cell)

        # Save the modified notebook
        self.save_notebook(notebook, notebook_path)

        return section_id

    def edit_section(self, notebook_path, section_id, new_title):
        # Load the notebook
        notebook = self.load_notebook(notebook_path)

        # Modify the title of the specified section
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown' and cell['source'].startswith(f'# Section {section_id}'):
                cell['source'] = f"# Section {section_id}\n\n{new_title}"
                break

        # Save the modified notebook
        self.save_notebook(notebook, notebook_path)

    def remove_section(self, notebook_path, section_id):
        # Load the notebook
        notebook = self.load_notebook(notebook_path)

        # Remove the section from the notebook
        notebook['cells'] = [cell for cell in notebook['cells'] if not (cell['cell_type'] == 'markdown' and cell['source'].startswith(f'# Section {section_id}'))]

        # Save the modified notebook
        self.save_notebook(notebook, notebook_path)

        # Remove the section from the internal list
        self.sections = [section for section in self.sections if section["id"] != section_id]

    def swap_sections(self, notebook_path, section_id_1, section_id_2):
        # Load the notebook
        notebook = self.load_notebook(notebook_path)

        # Swap the sections in the notebook
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown' and (cell['source'].startswith(f'# Section {section_id_1}') or cell['source'].startswith(f'# Section {section_id_2}')):
                cell['source'] = cell['source'].replace(f'{section_id_1}', 'TEMP_ID').replace(f'{section_id_2}', f'{section_id_1}').replace('TEMP_ID', f'{section_id_2}')

        # Save the modified notebook
        self.save_notebook(notebook, notebook_path)

    def add_resource(self, notebook_path, content):
        resource_id = len(self.resources) + 1
        self.resources.append({"id": resource_id, "content": content})

        # Load the notebook
        notebook = self.load_notebook(notebook_path)

        # Create a new code cell with the resource content
        new_cell = new_markdown_cell(content)

        # Add the new cell to the notebook
        notebook['cells'].append(new_cell)

        # Save the modified notebook
        self.save_notebook(notebook, notebook_path)

        return resource_id

    def edit_resource(self, notebook_path, resource_id, new_content):
        # Load the notebook
        notebook = self.load_notebook(notebook_path)

        # Find the resource cell and update its content
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown' and cell.metadata.get('resource_id') == resource_id:
                cell['source'] = new_content
                break

        # Save the modified notebook
        self.save_notebook(notebook, notebook_path)

    def remove_resource(self, notebook_path, resource_id):
        # Load the notebook
        notebook = self.load_notebook(notebook_path)

        # Remove the resource cell
        notebook['cells'] = [cell for cell in notebook['cells'] if cell.metadata.get('resource_id') != resource_id]

        # Save the modified notebook
        self.save_notebook(notebook, notebook_path)

        # Remove the resource from the internal list
        self.resources = [resource for resource in self.resources if resource["id"] != resource_id]

    def swap_resources(self, notebook_path, resource_id_1, resource_id_2):
        # Load the notebook
        notebook = self.load_notebook(notebook_path)

        # Swap resource cells
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown':
                if cell.metadata.get('resource_id') == resource_id_1:
                    cell.metadata['resource_id'] = resource_id_2
                elif cell.metadata.get('resource_id') == resource_id_2:
                    cell.metadata['resource_id'] = resource_id_1

        # Save the modified notebook
        self.save_notebook(notebook, notebook_path)
