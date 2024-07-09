#!/bin/bash
# sends a JSON POST request to the URL, then shows the body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
