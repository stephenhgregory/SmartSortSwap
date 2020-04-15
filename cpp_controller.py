import subprocess
import shlex
from pathlib import Path
import os


def compile_cpp_file(file_name, file_path=os.getcwd()):
    '''
    Compiles a cpp file "filename".

    Args:
        file_name (str): The name of the file to be compiled
        file_path (str): The absolute filepath (excluding the 
                            filename) of the .cpp file
    '''
    full_file_name = os.path.join(file_path, file_name)
    compile_command = 'g++ -Wall -std=c++11 ' + full_file_name + ' -o ' + Path(file_name).stem
    p = subprocess.Popen(shlex.split(compile_command),
                    stdout=subprocess.PIPE,
                    stdin=subprocess.PIPE)
    p.communicate()
    

def pass_args_to_cpp(executable_name, *args):
    '''
    Passes arguments to the 'stdin' buffer of a compiled executable.

    Args:
        executable_name (str): The name of the executable file to which we
                                want to write our arguments
        *args:                 The variable length list of arguments to be
                                passed to the executable

    '''
    process = subprocess.Popen(['./' + executable_name], 
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    for arg in args:
        process.stdin.write(repr(arg).encode('utf-8'))

