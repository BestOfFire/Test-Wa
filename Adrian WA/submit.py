import json
import cgi
from flask import Flask
app = Flask(__name__)
try:
    
    @app.route('/submit', methods=['POST'])
    def submit():
        form = cgi.FieldStorage()
        name = form.getvalue("name")
        rank = form.getvalue("rank")
        youtube = form.getvalue("youtube")
        form = cgi.FieldStorage()
        name = form.getvalue("name", "")
        rank = form.getvalue("rank", "")
        youtube = form.getvalue("youtube", "")

        print("Content-type: text/html")
        print()
        print("Name: " + name)
        print("Rank: " + rank)
        print("YouTube Link: " + youtube)

        data = {'name': name, 'rank': rank, 'youtube': youtube}
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

except Exception as e:
    print(e)
