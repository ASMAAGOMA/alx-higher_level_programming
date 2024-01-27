#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request
    u = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(u)as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
