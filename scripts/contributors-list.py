#!/usr/bin/env python
# This script generates the contributor list. 
# It is intended to run from the repository root, where it expects to find
# a file 'Contributors.py' that contains the name mapping.

import sys
from pylatexenc.latexencode import utf8tolatex
from run_or_die import run_or_die

try:
    from Contributors import Contributors
except Exception as e:
    Contributors = {}
    print('File "Contributors.py" not found. The script will only unify and sort the committer names.', file = sys.stderr)
    # print(e)

# Code:
def select_name(committer):
    for contributor, values in Contributors.items():
        if committer in values:
            return contributor
    return committer

def unify_contributors(committers):
    contributors = []
    for committer in committers:
        if len(committer) == 0: continue
        contributors.append(select_name(committer))
    return sorted(list(set(contributors))) # make sure entries are unique

# main:
results = run_or_die('git log --pretty="%an"', "Unable to query list of Git committers.")
committers = results[0].decode().split('\n') # convert bytes to unicode before breaking lines
contributors = ', '.join(unify_contributors(committers))
print(utf8tolatex(contributors))