import os
import fileinput
import sys
import pathlib
import re

# get the top directory to investigate
topDir = sys.argv[1]
firstFile = True
p = re.compile('.*\.java$')
totalFile = 0
hasJavaFile = False

for subdir, dirs, files in os.walk(topDir):
    # get the absolute path for the current directory
    dir = subdir[2:]
    dir = os.path.join(os.path.abspath(''), dir)

    for f in files:
        if p.match(f):
            hasJavaFile = True

            # get the absolute path for the current file
            fPath = os.path.join(dir, f)

            # calculate file size by number of line
            lineCount = 0
            for line in open(fPath):
                lineCount += 1

            if firstFile:
                with open("javaFileSize.txt", "w") as file:
                    file.write(f + "\n")
                firstFile = False
            else:
                with open("javaFileSize.txt", "a") as file:
                    file.write(f + "\n")

            with open("javaFileSize.txt", "a") as file:
                file.write("    Lines: " + str(lineCount) + "\n")
            totalFile += 1

    # only write to file the directory that contain java file
    if hasJavaFile:
        with open("javaFileSize.txt", "a") as file:
            file.write("Folder: " + subdir + "\n--------------------------------------------------------\n")
        hasJavaFile = False

with open("javaFileSize.txt", "a") as file:
    file.write("\nTotal file: " + str(totalFile))
