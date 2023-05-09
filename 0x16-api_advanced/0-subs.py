#!/usr/bin/python3
""" Query subscribers on a given Reddit subreddit """
import requests


def number_of_subscribers(subreddit):
    """ Return the total number of subscribers on a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    body = res.json().get("data")
    return body.get("subscribers")
