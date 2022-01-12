#!/bin/bash
# script that displays only the status code without using pipe
curl -s -i /dev/null -w "%{http_code}" "$1"
