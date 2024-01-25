#!/bin/bash
# Sends DELETE req to $1 URL and display response body
curl -s "$1" -X DELETE
