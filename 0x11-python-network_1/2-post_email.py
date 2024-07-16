#!/usr/bin/python3
"""sends post request to url with email in parameters """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = (urllib.parse.urlencode(values)).encode('ascii')
    request = urllib.request.Request(url,data)
    with urllib.request.urlopen(request) as response : 
        print(response.read().decode('utf-8'))

