#!/usr/bin/python3
"""
Sends a request to the specified URL
and displays the X-Request-Id value
from the header.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
