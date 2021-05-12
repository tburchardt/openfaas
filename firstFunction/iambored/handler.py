import requests
import os
import sys

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    r = requests.get("https://www.boredapi.com/api/activity/")
    return r.json().get("activity")
