from os import *

def get_files_info(working_directory, directory="."):
    full_path = path.join(working_directory, directory)
    abs_full_path = path.abspath(full_path)
    abs_path_working_directory = path.abspath(working_directory)
    
    if not path.abspath(full_path).startswith(abs_path_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'
    
    directory_contents = listdir(abs_full_path)
    lines_to_return = ""
    try:
        for item in directory_contents:
            item_info = f"- {item}: file_size={path.getsize(path.join(abs_full_path, item))} bytes, is_dir={path.isdir(path.join(abs_full_path, item))}"
            lines_to_return += item_info + "\n"
    except Exception as e:
        return f"Error: Unable to list directory '{directory}' - {str(e)}" 
    
    return lines_to_return.strip()

