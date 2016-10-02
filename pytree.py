#!/usr/bin/env python3
import subprocess
import sys
import os

# Initialize output variables
count_files = 0
count_dir = 0

# Get root directory for tree and first line of output
if len(sys.argv) == 1:
    cwd = os.getcwd()
    print(".")
else:
    cwd = sys.argv[1]
    print(cwd)


# List folder contents in sorted format
def listdir_nohidden_sorted(path):
    dir_content = [x for x in os.listdir(path) if not x.startswith('.')]
    return sorted(dir_content, key=str.lower)


# Recursive function
def tree(path, prepend=""):
    dir_content = listdir_nohidden_sorted(path)
    count_files = 0
    count_dir = 0

    for i, line in enumerate(dir_content):
        # If last element in directory, formating is different
        if i == len(dir_content) - 1:
            print(prepend + "└── " + str(line))
            subdir_prepend = "    "
        else:
            print(prepend + "├── " + str(line))
            subdir_prepend = "│   "
        if os.path.isfile(os.path.join(path, line)):
            count_files += 1
        else:
            count_dir += 1
            result = tree(os.path.join(path, line), prepend + subdir_prepend)
            count_files += result[0]
            count_dir += result[1]
    return count_files, count_dir

result = tree(cwd)
count_files += result[0]
count_dir += result[1]

# Summary
print("\n" + str(count_dir) + " directories, " + str(count_files) + " files")
