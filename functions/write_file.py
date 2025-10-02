from os import path, makedirs

def write_file(working_directory, file_path, content):
    full_path = path.join(working_directory, file_path)
    abs_full_path = path.abspath(full_path)
    abs_path_working_directory = path.abspath(working_directory)
    
    if not path.abspath(full_path).startswith(abs_path_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    dir_name = path.dirname(abs_full_path)
    print(f"Directory name: {dir_name}")
    if not path.exists(dir_name):
        try:
            makedirs(dir_name)  
        except Exception as e:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory - {str(e)}'
    
    with open(abs_full_path, 'w') as file:
        file.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'