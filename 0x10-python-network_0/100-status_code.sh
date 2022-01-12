#!/bin/bash
# script that displays only the status code without using pipe
curl -LI "$1" -w '%{http_code}\n' -s
