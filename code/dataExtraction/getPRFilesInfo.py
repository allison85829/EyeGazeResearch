# This script is originally written by Dyalan Tsuruda
# and later modified by Lien Quan for extracting useful information

# Standard Python libraries
import sys
import os
import pathlib

# Python GitHub API wrapper library
# https://github.com/sigmavirus24/github3.py
import github3

repo_owner = sys.argv[1]
repo_name = sys.argv[2]
directory = sys.argv[3]
filename_path_prefix = os.path.join(directory, sys.argv[3])

# When using this, replace USERNAME and PASSWORD with your GitHub username
# and password. (Yeah, it's probably not the most secure thing.)
github = github3.login("username", "password")
repository = github.repository(repo_owner, repo_name)
# get pull requests that are closed
pulls = repository.pull_requests(state="closed")

# Create a directory if it doesn't already exist
pathlib.Path(directory).mkdir(parents=True, exist_ok=True)

first_pull = True

for pull in pulls:
    pull_number = pull.number
    # get files that are related to the pull request
    files = pull.files()

    # variable that keep track of the number of file
    file_count = 1

    # iterate through file object to get file name and the changes in each file
    for file in files:
        file_name = str(file.filename)
        changes_count = str(file.changes_count)
        if first_pull:
            with open(filename_path_prefix + "PRFileInfo" + ".txt", "w") as file:
                try:
                    file.write("#" + str(pull_number) + "\nFile name: " + file_name + "\nChanges: "
                        + changes_count + "\n")
                except UnicodeEncodeError:
                    file.write("#" + str(pull_number) + " Comment " + str(comment_count) + ":\n"
                        + "--UnicodeEncodeError--" + "\n")

            first_pull = False
        else:
            with open(filename_path_prefix + "PRFileInfo" + ".txt", "a") as file:
                try:
                    file.write("#" + str(pull_number) + "\nFile name: " + file_name + "\nChanges: "
                        + changes_count + "\n")
                except UnicodeEncodeError:
                    file.write("#" + str(pull_number) + " Comment " + str(comment_count) + ":\n"
                        + "--UnicodeEncodeError--" + "\n")
        file_count += 1

    with open(filename_path_prefix + "PRFileInfo" + ".txt", "a") as file:
        file.write("Number of files: " + str(file_count) + "\n\n")
