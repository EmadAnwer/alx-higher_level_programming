#!/usr/bin/python3
"""  script that fetches https://alx-intranet.hbtn.io/status using requests"""

if __name__ == "__main__":
    import requests
    import sys
    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])
