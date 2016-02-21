import requests

def istheinternetonfire(query):
    r = requests.get('https://www.istheinternetonfire.com/status.txt')
    return r.content
