import urllib.request
import json

with urllib.request.urlopen("http://www.projectdoama.com/api/v1/getMovieInfo/Harry") as response:
    html = response.read()

output = html.decode('utf-8')

obj = json.loads(output)

for item in obj:
    print(obj)
