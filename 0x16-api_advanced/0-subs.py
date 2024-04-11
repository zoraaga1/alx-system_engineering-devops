#!/usr/bin/python3

"""
This module queries the Reddit API
to get the number of subscribers for a given subreddit.
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        The number of subscribers for the subreddit.
        Returns 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
