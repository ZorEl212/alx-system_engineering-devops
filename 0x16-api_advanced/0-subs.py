#!/usr/bin/python3
"""Get Number of subscribers of a subreddit"""

import requests
from sys import argv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}


def number_of_subscribers(subreddit):
    """"Get Subreddit subs number"""
    req = requests.get(f"https://reddit.com/r/{subreddit}/about.json",
                       headers=headers)
    if ((list(req.json().values())[0]) == 't5'):
        data = dict(list(req.json().values())[1])['subscribers']
        return data
    else:
        return 0
