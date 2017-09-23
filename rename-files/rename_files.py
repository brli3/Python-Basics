"""
Rename files and directories
a. lowercase
b. replace space with "_" for files and "-" for directories
put this script in the directory and run it
"""
import os
path = os.getcwd()
filenames = os.listdir(path)
print('Current path:', path)
ifile = 0
idir = 0
for filename in filenames:
    if os.path.isfile(filename):
        os.rename(filename, filename.replace(" ", "_").lower())
        ifile += 1
    elif os.path.isdir(filename):
        os.rename(filename, filename.replace(" ", "-").lower())
        idir += 1
    else:
        pass
print("No. of files:", ifile)
print("No. of directories:", idir)

