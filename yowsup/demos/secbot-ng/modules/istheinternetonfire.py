import requests

def istheinternetonfire(query):
    if query.split(' ')[0] == "help":
        h = "Find out if the internet is on fire..."
        return h

    else:
        r = requests.get('https://www.istheinternetonfire.com/status.txt')
        return r.content
