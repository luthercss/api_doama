import urllib.request

with urllib.request.urlopen("http://www.projectdoama.com/api/v1/getMovieInfo/Harry") as response:
    html = response.read()

print(html)

