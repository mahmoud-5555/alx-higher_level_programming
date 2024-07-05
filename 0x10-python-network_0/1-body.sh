#!/bin/bash
# Check the args
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL argument
URL=$1

# Send a GET request
response=$(curl -s -o /dev/stdout -w "%{http_code}" "$URL")

# Extract the HTTP status code and response body
http_status=${response: -3}
body=${response::-3}

# Check if the status code is 200 (OK)
if [ "$http_status" -eq 200 ]; then
    echo "$body"
