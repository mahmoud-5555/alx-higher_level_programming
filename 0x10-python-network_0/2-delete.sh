#!/bin/bash
# Check args
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL argument
URL=$1

# Send a DELETE request to the URL using curl and store the response body
response=$(curl -s -X DELETE "$URL")

# Display the response body
echo "$response"
