#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.error
    u = sys.argv[1]
    try:
        with urllib.request.urlopen(u)as response:
            print(response.read())
    except urllib.error.HTTPError as e:
        print("\t- Error code:", e.code)
