#!/bin/bash
# Check if URL argument is provided

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL argument
URL=$1

# Send an OPTIONS request
methods=$(curl -s -X OPTIONS -i "$URL" | grep -i Allow | awk -F ": " '{print $2}' | tr -d '\r\n')

# Check if the Allow header is present and display the methods
if [ -n "$methods" ]; then
    echo "$methods"
fi
