#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
if [ $(curl -Gs -o  /dev/null -w "%{http_code}" "${1}") -eq 200 ]; then curl -s -G "${1}"; fi
