#!/usr/bin/python3
"""Query Reddit API and print top ten hot posts of a subreddit"""
import re
import requests


def add_title(a_dict, hot_posts):
    """ Add titles to a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in a_dict.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                a_dict[key] += 1
    hot_posts.pop(0)
    add_title(a_dict, hot_posts)


def recurse(subreddit, a_dict, after=None):
    """ Query to Reddit API """
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
    add_title(a_dict, hot_posts)
    after = body['data']['after']
    if not after:
        return
    recurse(subreddit, a_dict, after=after)


def count_words(subreddit, word_list):
    """ Wrap recurse function """
    a_dict = {}

    for word in word_list:
        a_dict[word] = 0

    recurse(subreddit, a_dict)
    l = sorted(a_dict.items(), key=lambda kv: kv[1]).reverse()
    if len(l) != 0:
        for item in l:
            if item[1] is not 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
