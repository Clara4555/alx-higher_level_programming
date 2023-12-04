#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    res = requests.get(url)
    commit = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commit[i].get("sha"),
                commit[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
