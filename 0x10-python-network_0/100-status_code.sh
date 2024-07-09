#!/bin/bash
#will return only the status code of the ip in argument
curl -o /dev/null -s -w "%{http_code}\n" $1
