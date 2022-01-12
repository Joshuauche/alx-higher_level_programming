#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -s -d '{"name":"John Doe", "age":33}' -X POST "$1" 
