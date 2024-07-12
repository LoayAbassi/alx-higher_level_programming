#!/usr/bin/python3
"""fetches the give url"""
import urllib.request

if __name__== "__main__" : 

    url = "https://alx-intranet.hbtn.io/status"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("type: ",type(body) )
        print("content: ",body)
        print("utf8 content: ",body.decode("utf-8"))

