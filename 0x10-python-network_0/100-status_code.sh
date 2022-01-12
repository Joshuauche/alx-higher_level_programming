#!/bin/bash
# script that displays only the status code without using pipe
curl -LI 34.138.172.1 -w '%{http_code}\n' -s
