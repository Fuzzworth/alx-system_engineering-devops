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

    results = response.json().get("data")
    count += results.get("dist")
    for child in results.get("children"):
        title = child.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([x for x in title if x == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if results.get("after") is None:
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
    else:
        count_words(subreddit, word_list, instances, after, count)
