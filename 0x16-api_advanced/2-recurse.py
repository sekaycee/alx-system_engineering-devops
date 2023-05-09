#!/usr/bin/python3
"""Query a list of all hot posts on a given Reddit subreddit"""
import requests


def add_title(hot_list, hot_posts):
    """ Add item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """ Query Reddit API """
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'after': after
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return None

    body = res.json()
    hot_posts = body['data']['children']
    add_title(hot_list, hot_posts)
    after = body['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
