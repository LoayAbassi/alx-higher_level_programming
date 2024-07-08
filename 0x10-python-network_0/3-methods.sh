#!/bin/bash
#this will show the list of possible methods a url can accept
curl -sL -i $1 | grep -i "Allow:" |cut -d ' ' -f2-
