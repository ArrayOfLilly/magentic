from os import path
import subprocess

def run_python_file(working_directory, file_path, args=[]):    
    full_path = path.join(working_directory, file_path)
    abs_full_path = path.abspath(full_path)
    abs_path_working_directory = path.abspath(working_directory) 
    
    if not path.abspath(full_path).startswith(abs_path_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not path.exists(abs_full_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    captured_stdout = ""
    captured_stderr = ""
    try:
        completed_process = subprocess.run(
            ['python', abs_full_path] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        
        lines_to_return = ""
        return_code = completed_process.returncode
        if return_code != 0:
            lines_to_return += f"Process exited with code {return_code}\n"
        if completed_process.stdout:
            lines_to_return += f"STDOUT:{completed_process.stdout}\n"
        lines_to_return += "No output produced.\n"
        lines_to_return += f"STDERR:{completed_process.stderr}\n"
    except Exception as e:
        return f"Error: executing Python file: {e}" 
    
    return lines_to_return.strip()