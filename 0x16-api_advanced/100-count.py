#!/usr/bin/python3
""" recursive module"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively counts the occurrences of keywords
    in the titles of all hot articles for a given subreddit.

    Args:
    - subreddit (str): The subreddit to fetch hot articles from.
    - word_list (list): A list of keywords to count occurrences for.
    - after (str): The 'after' token for pagination.
    - counts (dict): A dictionary to store the counts of keywords.

    Returns:
    - None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after} if after else {"limit": 100}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        if not children:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word.lower()}: {count}")
            return
        for child in children:
            title = child["data"]["title"]
            words = title.lower().split()
            for word in word_list:
                if word.lower() in words:
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1
        after = data["data"]["after"]
        count_words(subreddit, word_list, after, counts)
    else:
        return
