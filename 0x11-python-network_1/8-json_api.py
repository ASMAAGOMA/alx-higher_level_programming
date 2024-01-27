#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
if __name__ == "__main__":
    import sys
    import requests
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    value = {"q", letter}
    r = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        if r.json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json.get("id"), r.json.get("name")))
    except ValueError:
        print("Not a valid JSON")
