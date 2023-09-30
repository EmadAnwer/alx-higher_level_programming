#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)"""

if __name__ == "__main__":
    import requests
    import sys
    req = requests.get(f'https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits')
    for commit in req.json()[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
