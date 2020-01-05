"""
Lesson 06 Activity : Github Api
"""

import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    USERNAME = sys.argv[1]

    # 1. Retrieve a list of "events" associated with the given user name
    RESPONSE = requests.get('https://api.github.com/users/{}/events'
                            .format(USERNAME))
    EVENTS = json.loads(RESPONSE.content)

    # 2. Print out the time stamp associated with the first event in that list.
    # print(json.dumps(events, indent=4, sort_keys=True))
    print(EVENTS[0]['created_at'])
