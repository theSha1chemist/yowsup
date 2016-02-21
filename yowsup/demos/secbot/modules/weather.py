import requests
import time
import json

def weather(query):
    if query.split(' ')[0] == "help":
        h = "Return the current weather by location"
        return h

    else:
        url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&APPID=23309f546e6cb92b597c47ff1e9ce1f2&q=%s' % (query)
        r = requests.get(url)
        parsed_json = json.loads(r.content)

        description = parsed_json['weather'][0]['description']
        temp = parsed_json['main']['temp']
        sunrise = time.ctime(int(parsed_json['sys']['sunrise'])).split()[3]
        sunset = time.ctime(int(parsed_json['sys']['sunset'])).split()[3]

        return str({'description':description, 'temp degrees C':temp, 'sunrise':sunrise, 'sunset':sunset})
