#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

if __name__ == "__main__":
    import sys
    import requests
    username, token = sys.argv[1:]
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-Github-Api-Version": "2022-11-28"
    }
    url = f"https://api.github.com/user"
    with requests.get(url, headers=headers) as response:
        body = response.json()
        print(body.get("id"))