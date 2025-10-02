from os import path
# from config import MAX_READ_SIZE

MAX_READ_SIZE = 10000

def get_file_content(working_directory, file_path="."):
    full_path = path.join(working_directory, file_path)
    abs_full_path = path.abspath(full_path)
    abs_path_working_directory = path.abspath(working_directory) 
    
    if not path.abspath(full_path).startswith(abs_path_working_directory):
        return f'Error: Cannot read "{abs_full_path}" as it is outside the permitted working directory'
    if not path.isfile(abs_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_full_path, 'r') as file:
            content = file.read(MAX_READ_SIZE)
            if len(content) == MAX_READ_SIZE:
                content += f'[...File "{file_path}" truncated at 10000 characters]'
            return content 
    except Exception as e:
        return f'Error: Unable to read file "{file_path}" - {str(e)}'   
    