#!/bin/bash
#displays body of response
curl -sL -w "%{http_code}" "$1" -o temp_body | grep -q 200 && cat temp_body && rm temp_body
