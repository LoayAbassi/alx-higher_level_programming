#!/bin/bash
#displays size of file curled
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f 2