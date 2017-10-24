import urllib.request
import json
import requests
from flask import Flask, request, Response

app = Flask(__name__)
@app.route("/")
def index():
    page = "<h1>You will see some Harry Porter stuff</h1>"
    page += "<button><a href ='/HarryPorter'>Click</a></button"
    return page

@app.route("/HarryPorter")
def HarryPorterInfo():
    rec = requests.get("http://www.projectdoama.com/api/v1/getMovieInfo/Harry")
    data = json.loads(rec.text)
    page = "<h1>Some Harry Porter movies we have on the server</h1>"
    page += "<ul>"
    for item in data:
        page +="<li>%s</li>"%item['title']
    page +="</ul>"
    return page

app.run(debug=True)
