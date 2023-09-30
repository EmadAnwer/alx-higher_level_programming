#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)"""

if __name__ == "__main__":
    import requests
    import sys
    headers = {'X-GitHub-Api-Version': '2022-11-28',
               'Accept': 'application/vnd.github.v3+json'}
    payload = {'per_page': 10, 'page': 1}
    req = requests.get(
        f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits',
        headers=headers,
        params=payload)
    for commit in req.json():
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
