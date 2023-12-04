#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
You must use Basic Authentication with a personal access token as password
to access to your information (only read:user permission is needed)
The first argument will be your username
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    respon = requests.get("https://api.github.com/user", auth=auth)
    print(respon.json().get("id"))
