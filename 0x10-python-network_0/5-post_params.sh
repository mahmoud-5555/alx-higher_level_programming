#!/bin/bash
# Check the URL 
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# take args
URL=$1

# Variables to be sent in the POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request to the URL with variables using curl
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$URL")

# Display the response body
echo "$response"
