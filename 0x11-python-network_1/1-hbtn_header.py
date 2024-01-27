#!/usr/bin/python3
"""
    Python script that takes in a URL,
    sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response.
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    u = sys.argv[1]
    with urllib.request.urlopen(u)as response:
        header = response.getheader("X-Request-Id")
        print(header)
