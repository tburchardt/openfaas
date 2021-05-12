import os
import requests
import sys

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    gateway_hostname = os.getenv("gateway_hostname", "gateway") 
    if(req == "something to do"):
        r = requests.get("http://gateway.openfaas:8080/function/iambored") 
        return r.text
    if(req == "advise about life"):
        r = requests.get("http://gateway.openfaas:8080/function/advise") 
        return r.text
    if(req == "cat facts"):
        r = requests.get("http://gateway.openfaas:8080/function/cats") 
        return r.text
    if(req == "a tesla"):
        r = requests.get("http://gateway.openfaas:8080/function/dodecoin") 
        return r.text
    if(req == ""):
        return "Tell what you need :) I am your virtual butler"
    
    
    return "Error"
  