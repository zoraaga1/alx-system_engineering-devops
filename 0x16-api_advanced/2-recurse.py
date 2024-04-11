#!/usr/bin/python3
"""recure module"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches titles of all hot articles for a given subreddit.

    Args:
    - subreddit (str): The subreddit to fetch hot articles from.
    - hot_list (list): A list to store the titles of hot articles.
    - after (str): The 'after' token for pagination.

    Returns:
    - list: A list containing the titles of all hot articles for the subreddit,
            or None if the subreddit is not found or empty.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after} if after else {"limit": 100}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        if not children:
            return hot_list
        hot_list.extend([child["data"]["title"] for child in children])
        after = data["data"]["after"]
        return recurse(subreddit, hot_list, after)
    else:
        return None
