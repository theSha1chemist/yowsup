import requests

def isTheInternetOnFire():
    r = requests.get('https://www.istheinternetonfire.com/status.txt')
    return r.content
