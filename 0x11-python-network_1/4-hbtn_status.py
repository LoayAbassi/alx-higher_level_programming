#!/usr/bin/python3
"""fetches the given url using request package and shows body of response"""
import requests
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    response = requests.get(url, header)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
