#!/bin/bash
# script that displays only the status code without using pipe
curl -so -i / dev/null -w "%{http_code}" "$1"
