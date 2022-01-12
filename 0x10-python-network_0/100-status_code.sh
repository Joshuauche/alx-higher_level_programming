#!/bin/bash
# script that displays only the status code without using pipe
curl -R -s -S -w  "%{http_code}\n" "$1"