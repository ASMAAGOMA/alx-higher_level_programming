#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests
    u = "https://alx-intranet.hbtn.io/status"
    with requests.get(u)as response:
        body = response.text
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
