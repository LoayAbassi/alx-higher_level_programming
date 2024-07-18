#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty"""

if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    
    try:
        r = requests.post(url, data={"q": q})
        r_json = r.json()
        if r_json:
            print("[{}] {}".format(r_json["id"], r_json["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
