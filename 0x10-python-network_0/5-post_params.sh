#!/bin/bash
# sends a POST request to the URL along with 2 variables and displays body of response
curl -s -X POST -d "email : test@gmail.com & subject = I will always be here for PLD" $1
