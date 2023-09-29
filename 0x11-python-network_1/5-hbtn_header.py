#!/usr/bin/python3
"""displays the value of the variable X-Request-Id"""

if __name__ == "__main__":
    import requests
    import sys
    req = requests.get(sys.argv[1])
    print(req.headers["X-Request-Id"])
