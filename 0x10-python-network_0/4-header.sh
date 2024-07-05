#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL argument
URL=$1

# Send a GET request to the URL with custom header using curl
response=$(curl -s -H "X-School-User-Id: 98" "$URL")

# Display the response body
echo "$response"
