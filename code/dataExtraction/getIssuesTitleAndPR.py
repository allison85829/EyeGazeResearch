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
# take the fourth argument as the issue label
label = sys.argv[4]
filename_path_prefix = os.path.join(directory, sys.argv[3])

github = github3.login("username", "password")
repository = github.repository(repo_owner, repo_name)

# get issues that are closed and have specific label
issues = repository.issues(state="closed", labels=label)

pathlib.Path(directory).mkdir(parents=True, exist_ok=True)

first_issue = True

for issue in issues:
    issue_number = issue.number
    issue_title = str(issue.as_dict().get("title"))
    
    # only list issues that have associate pull request
    pull = issue.pull_request()

    if first_issue:
        with open(filename_path_prefix + label + "TitleAndPR" + ".txt", "w") as file:
            file.write("Issues Labeled \"" + label + "\"\n")
            if str(pull) != "None":
                pull_title = str(pull.title)
                pull_number = str(pull.number)

                file.write("#" + str(issue_number) + ": " + issue_title + "\n")
                file.write("    Pull Request #" + pull_number + ": " + pull_title + "\n\n")

        first_issue = False
    else:
        with open(filename_path_prefix + label + "TitleAndPR" + ".txt", "a") as file:
            if str(pull) != "None":
                pull_title = str(pull.title)
                pull_number = str(pull.number)

                file.write("#" + str(issue_number) + ": " + issue_title + "\n")
                file.write("    Pull Request #" + pull_number + ": " + pull_title + "\n\n")
