import requests
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur")
    result = f"One Bitcoin is worth {(r.json().get('bitcoin').get('eur'))/39000} teslas"
    return result    
