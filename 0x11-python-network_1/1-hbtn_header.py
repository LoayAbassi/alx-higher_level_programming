#!/usr/bin/python3
"""sends request to URL => displays value of
X-Request-Id variable found in the header of the response."""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(response.headers["X-Request-Id"])
