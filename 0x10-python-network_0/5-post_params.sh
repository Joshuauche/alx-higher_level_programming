#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response, with a variable email and subject
curl -s -d "email: test@gmail.com" -d "subject: I will always be here for PLD" -X POST "$1" 
