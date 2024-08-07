#!/usr/bin/python3
"""sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    request = requests.get(url)
    print(request.headers["X-Request-Id"])
