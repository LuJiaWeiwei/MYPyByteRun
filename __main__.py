"""A main program for Byterun."""

import argparse
import logging
import sys
import os

#Add a path to identify the module under the current path
sys.path.append(os.getcwd())
#sys.path.append("/home/2015jsj/2015112118/byterun/byterun")
import execfile


#Use the argparser module to analyze the parameters of the run, and give a hint when there is a help option
parser = argparse.ArgumentParser(
    prog="byterun",
    description="Run Python programs with a Python bytecode interpreter.",
)

#True with the -m option
parser.add_argument(
    '-m', dest='module', action='store_true',
    help="prog is a module name, not a file name.",
)
parser.add_argument(
    '-d', dest='detail', action='store_true',
    help="see the details in the execution of the program"
)
parser.add_argument(
    '--step', dest='step', action='store_true',
    help="get every step of executing progam"
)
parser.add_argument(
    '-v', '--verbose', dest='verbose', action='store_true',
    help="trace the execution of the bytecode.",
)
parser.add_argument(
    'prog',
    help="The program to run.",
)
parser.add_argument(
    'args', nargs=argparse.REMAINDER,
    help="Arguments to pass to the program.",
)
args = parser.parse_args()

#With a large module as a unit, the current unrealized
if args.module:
    print("Sorry the module part has not completed yet!")
    args.prog = raw_input("you can input a python file name:")

# Directly assigned to analyze a single file function
run_fn = execfile.run_python_file

# Enable INFO mode, use the log.info() output message in the pyvm file
if args.step:
    level = logging.DEBUG
elif args.detail:
    level = logging.INFO
else:
    level = logging.WARNING
logging.basicConfig(level=level)

# Args and argv variables in the new function
argv = [args.prog] + args.args
run_fn(args.prog, argv)
