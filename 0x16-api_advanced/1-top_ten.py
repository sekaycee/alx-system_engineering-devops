#!/usr/bin/python3
""" Print hot posts on a given Reddit subreddit """
import requests


def top_ten(subreddit):
    """ Print the titles of the 10 hottest posts on a given subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "limit": 10
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    body = res.json()
    hot_posts = body['data']['children']
    if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
