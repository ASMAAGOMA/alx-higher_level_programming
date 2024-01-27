#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import requests
    import sys
    u = sys.argv[1]
    with requests.get(u)as response:
        if response.ok:
            print(response.text)
        else:
            print(f"Error code: {response.status_code}")
