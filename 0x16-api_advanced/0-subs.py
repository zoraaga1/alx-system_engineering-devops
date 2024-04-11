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
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
