import requests
import random
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    return r.json()[random.randint(0, 3)].get("text")
