#!/bin/bash
curl -s -I "$1" | grep Allow | sed 's/^Allow: //'