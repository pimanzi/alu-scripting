#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
 returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit,
    or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'python3:0-subs:v1.0 (by /u/yourusername)'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    else:
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
