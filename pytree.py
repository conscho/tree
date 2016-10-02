#!/usr/bin/env python3
import sys
import os
import re


# Weird sorting
def weird_sort(input):
    return re.sub('[^a-zA-Z0-9]', '', input).lower()


# List folder contents in sorted format
def listdir_nohidden_sorted(path):
    dir_content = [x for x in os.listdir(path) if not x.startswith('.')]
    return sorted(dir_content, key=weird_sort)


# Recursive function
def tree(path, prepend=""):
    dir_content = listdir_nohidden_sorted(path)
    count_dir = 0
    count_files = 0

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
            count = tree(os.path.join(path, line), prepend + subdir_prepend)
            count_dir += count[0] + 1
            count_files += count[1]
    return count_dir, count_files

# Output
if len(sys.argv) == 1:
    cwd = os.getcwd()
    print(".")
else:
    cwd = sys.argv[1]
    print(cwd)
count = tree(cwd)
print("\n" + str(count[0]) + " directories, " + str(count[1]) + " files")
