#!/usr/bin/python3
"""Sends a request, shows result in body of response (handeling exceptions )"""
import urllib.error
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as er:
        print("Error code:", er.status)