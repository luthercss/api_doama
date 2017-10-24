import requests
import json

rec = requests.get("http://www.projectdoama.com/api/v1/getMovieInfo/Harry")

#print(rec.text)

#rec.text is in JSON format, and can be parsed with json module

data = json.loads(rec.text)

print(data[0]["title"])
