import requests
import json

def ud(query):
    r = requests.get('http://api.urbandictionary.com/v0/define?term=%s' % (query))
    data = json.loads(r.content)
    definition = data['list'][0]['definition']
    return definition
