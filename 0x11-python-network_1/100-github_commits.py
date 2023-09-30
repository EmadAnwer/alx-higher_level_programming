#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)"""

if __name__ == "__main__":
    import requests
    import sys
    req = requests.get(
        f'https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits')
    for commit in range(10):
        try:
            print(req.json()[commit].get('sha'), end=': ')
            print(req.json()[commit].get('commit').get('author').get('name'))
        except:
            pass
