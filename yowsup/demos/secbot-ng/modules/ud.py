import requests
import json

def ud(query):
    if query.split(' ')[0] == "help":
        h = "Urban Dictionary is a satirical crowdsourced online dictionary of slang words and phrases that was founded in 1999 as a parody of Dictionary.com"
        return h

    else:
        r = requests.get('http://api.urbandictionary.com/v0/define?term=%s' % (query))
        data = json.loads(r.content)
        try:
            definition = data['list'][0]['definition']
            return definition

        except IndexError:
            return "No results..."


