#!/usr/bin/env python3
import subprocess
import sys
import os

# Initialize output variables
output = ""
count_files = 0
count_dir = 0

# Get root directory for tree and first line of output
if len(sys.argv) == 1:
    cwd = os.getcwd()
    output += ".\n"
else:
    cwd = sys.argv[1]
    output += str(cwd) + "\n"

# Recursive function
def tree(cwd, prepend=""):
    dir_output = ""
    dir_content = [x for x in os.listdir(cwd) if not x.startswith('.')]
    count_files = 0
    count_dir = 0

    for i, line in enumerate(dir_content):
        # If last element in directory, formating is different
        if i == len(dir_content) - 1:
            dir_output += prepend + "└── " + str(line) + "\n"
            subdir_prepend = "    "
        else:
            dir_output += prepend + "├── " + str(line) + "\n"
            subdir_prepend = "│   "

        if os.path.isfile(os.path.join(cwd, line)):
            count_files += 1
        else:
            count_dir += 1
            result = tree(os.path.join(cwd, line), prepend + subdir_prepend)
            dir_output += result[0]
            count_files += result[1]
            count_dir += result[2]
    return dir_output, count_files, count_dir

result = tree(cwd)
output += result[0]
count_files += result[1]
count_dir += result[2]

# Summary
output += "\n" + str(count_dir) + " directories, " + str(count_files) + " files"

print(output)
