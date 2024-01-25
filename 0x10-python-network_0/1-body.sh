#!/bin/bash
# Sends GET req to URL and display response body

curl -sfL "$1" -X GET
