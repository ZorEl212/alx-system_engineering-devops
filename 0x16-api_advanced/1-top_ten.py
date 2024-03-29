#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    req = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)
    if req.status_code == 200:
        [print(child.get("data").get("title"))
         for child in req.json().get("data").get("children")]
    else:
        print('None')
