#!/bin/bash
# Status code
curl -s -o /dev/null -I -w "%{http_code}" "$1"
./100-status_code.sh 0.0.0.0:5000 ; echo ""
