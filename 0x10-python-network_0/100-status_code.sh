#!/bin/bash
# script that displays only the status code without using pipe
curl -R -s "$1" -S -w  "%{http_code}\n" 
