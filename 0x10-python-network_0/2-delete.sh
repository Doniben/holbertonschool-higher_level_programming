#!/bin/bash
# Sends a DELETE request to the URL passed as first argument. Displays the body of the response.
curl curl -s -X "DELETE" "$1"
