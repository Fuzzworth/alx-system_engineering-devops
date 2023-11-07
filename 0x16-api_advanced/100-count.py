#!/usr/bin/python3
"""
Module Docs
"""
import requests


def count_words(subreddit, word_list, instances={}, count=0, after=""):
    """
    Function Docs
    """
    url = 'https://www.reddit.com'
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    response = requests.get(
            '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
                url, subreddit, 'hot', 100, count, after),
            headers=header,
            allow_redirects=False)
    try:
        if response.status_code != 200:
            raise Exception
    except Exception:
        print("")
        return None

    if not instances:
        for word in word_list:
            if word.lower() not in instances:
                instances[word.lower()] = 0

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(
                instances.items(),
                key=lambda key_value: (-key_value[1], key_value[0])
                )
        for instance in instances:
            if instance[1]:
                print("{}: {}".format(instance[0], instance[1]))
        return None
    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in instances.keys():
                instances[word] += lower.count(word)

    except Exception:
        return None
    count_words(subreddit, word_list, instances, count, after)
