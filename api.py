import urllib.request
import json
import requests
from flask import Flask, request, Response

app = Flask(__name__)
@app.route("/")
def index():
    page ="<title>HP</title>"
    page += "<h1>You will see some Harry Potter stuff</h1>"
    page += "<form action ='/HarryPotter'><input type='submit' value ='Click for HP'></input></form>"
    return page

@app.route("/HarryPotter")
def HarryPorterInfo():
    rec = requests.get("http://www.projectdoama.com/api/v1/getMovieInfo/Harry")
    data = json.loads(rec.text)
    page = "<title>HP</title>"
    page += "<h1>Some Harry Potter movies we have on the server</h1>"
    page += "<ul>"
    for item in data:
        page +="<li>%s</li>"%item['title']
    page +="</ul>"
    page += "<form action ='/'><input type='submit' value ='Back'></input></form>"
    return page

app.run(debug=True)
