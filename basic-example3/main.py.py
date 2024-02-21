# # main.py

# from kk import SynthesisManager

# # Create an instance of SynthesisManager
# manager = SynthesisManager()

# # Function to add a section to the specified notebook
# def add_section(notebook_path):
#     section_id = manager.create_and_add_section_then_return_id(notebook_path, "Introduction")
#     print(f"Section {section_id} added to the notebook at: {notebook_path}")

# if __name__ == "__main__":
#     # Provide the path to the notebook file
#     notebook_path = "Untitled.ipynb"
#     add_section(notebook_path)


# main.py

from synthesizeManager.synthesize_manager import SynthesisManager

def main():
    # Instantiate SynthesisManager
    manager = SynthesisManager()

    # Path to the notebook file
    notebook_path = "Untitled.ipynb"

    # # Add a section to the notebook
    # section_id = manager.create_and_add_section_then_return_id(notebook_path, "Introduction")
    # print(f"Section {section_id} added to the notebook at: {notebook_path}")

    # # # Edit a section in the notebook
    # # manager.edit_section(notebook_path, section_id, "Updated Introduction")
    # # print(f"Section {section_id} edited in the notebook at: {notebook_path}")

    # # Remove a section from the notebook
    # manager.remove_section(notebook_path, section_id)
    # print(f"Section {section_id} removed from the notebook at: {notebook_path}")

    # # Swap sections in the notebook
    # section_id_1 = manager.create_and_add_section_then_return_id(notebook_path, "Section 1")
    # section_id_2 = manager.create_and_add_section_then_return_id(notebook_path, "Section 2")
    # manager.swap_sections(notebook_path, section_id_1, section_id_2)
    # print(f"Sections {section_id_1} and {section_id_2} swapped in the notebook at: {notebook_path}")
    # resource_id = manager.add_resource(notebook_path, "# Resource Title\n\nThis is the content of the resource.")
    # print(f"Resource {resource_id} added to the notebook at: {notebook_path}")

    # # Edit a resource in the notebook
    # manager.edit_resource(notebook_path, resource_id, "# Updated Resource Title\n\nThis is the updated content of the resource.")
    # print(f"Resource {resource_id} edited in the notebook at: {notebook_path}")

    # # Remove a resource from the notebook
    # manager.remove_resource(notebook_path, resource_id)
    # print(f"Resource {resource_id} removed from the notebook at: {notebook_path}")

    # # Swap resources in the notebook
    resource_id_1 = manager.add_resource(notebook_path, "# Resource 1\n\nContent of Resource 3")
    resource_id_2 = manager.add_resource(notebook_path, "# Resource 2\n\nContent of Resource 4")
    manager.swap_resources(notebook_path, resource_id_2, resource_id_1)
    print(f"Resources {resource_id_1} and {resource_id_2} swapped in the notebook at: {notebook_path}")

if __name__ == "__main__":
    main()
