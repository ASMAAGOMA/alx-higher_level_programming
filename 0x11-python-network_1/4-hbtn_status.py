#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests
    u = "https://alx-intranet.hbtn.io/status"
    with requests.get(u)as response:
        body = response.txt
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
