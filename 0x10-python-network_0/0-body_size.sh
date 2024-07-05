#!/bin/bash
# Check args
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL argument
URL=$1

# Send a GET request
response=$(curl -sI "$URL" | grep -i content-length | awk '{print $2}')

# print output 
echo $response
