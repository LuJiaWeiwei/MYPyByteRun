"""Execute files of Python code."""

import dis
import imp
import os
import sys
import tokenize

sys.path.append(os.getcwd())
#sys.path.append("/home/2015jsj/2015112118/byterun/byterun")
#sys.path.append("/home/2015jsj/2015112118/byterun")
from pyvm2 import VirtualMachine

NoSource = Exception

def exec_code_object(code, env):
    vm = VirtualMachine()
    vm.run_code(code, f_globals=env)

# In python2 and python3, buitins map different keys
try:
    BUILTINS = sys.modules['__builtin__']
except KeyError:
    BUILTINS = sys.modules['builtins']


def run_python_file(filename, args, package=None):
    '''
    Run a python file as the main program
    `filename` is the path to it
    `args` is treated as argv
    `package` for the package, temporarily not considered
    '''

    # Create a module to serve as __main__
    old_main_mod = sys.modules['__main__']
    main_mod = imp.new_module('__main__')
    sys.modules['__main__'] = main_mod
    main_mod.__file__ = filename
    main_mod.__builtins__ = BUILTINS

    # Set sys.argv and the first path element properly.
    old_argv = sys.argv
    old_path0 = sys.path[0]

    sys.argv = args
    # When filename is run as a full path, dirname () will return the full
    # path where the file was changed
    # When running in a relative path, return an empty directory
    sys.path[0] = os.path.abspath(os.path.dirname(filename))

    try:
        # Open the target file
        try:
            source_file = open(filename, 'rU')
        except IOError:
            raise NoSource("No file to run: %r" % filename)

        try:
            source = source_file.read()
        finally:
            source_file.close()

        # compile() source code will be compiled into bytecode, the source code
        # needs a blank line.
        if not source or source[-1] != '\n':
            source += '\n'
        code = compile(source, filename, "exec")

        #dis() function decompile into assembly code
        # Jump to pyvm.py in the implementation
        exec_code_object(code, main_mod.__dict__)

    finally:
        # Restore the old __main__
        sys.modules['__main__'] = old_main_mod

        # Restore the old argv and path
        sys.argv = old_argv
        sys.path[0] = old_path0
