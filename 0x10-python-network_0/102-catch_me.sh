#!/bin/bash
#this sends a request and waits for the server to respond with 'u got me'
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
