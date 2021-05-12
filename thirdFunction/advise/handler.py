import requests
import random
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    r = requests.get("https://api.adviceslip.com/advice")
    return r.json().get("slip").get("advice")
