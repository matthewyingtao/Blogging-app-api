from flask import Flask, request
from replit import db
import difflib
import os
import json
from datetime import datetime
from collections import OrderedDict

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

def isNewTitle(key):
    if key in db.keys():
        return False
    else:
        return True


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "You shouldn't be here."
    if request.method == 'POST':
        data = request.get_json(force=True)
        if isNewTitle(data['title']):
            data['likes'] = "0"
            data['date']= datetime.now().timestamp()
            db[data['title']] = data
            return "Added Successfully!"
        else:
            return "An error has occurred"
    return "hi bot"

@app.route('/posts')
def posts():
    keys = db.keys()
    post_dict = {}
    for key in keys:
        post_dict[key] = db[key]
    sorted_keys = sorted(post_dict, key=lambda x: (post_dict[x]['date']), reverse=True)
    sorted_data = OrderedDict()
    for key in sorted_keys:
        sorted_data[key] = post_dict[key]
    return json.dumps(sorted_data)

@app.route('/search/<word>')
def search(word):
    titles = list(db.keys())
    search_word = word.replace(" ", "")
    nearest_titles = difflib.get_close_matches(search_word, titles)
    close_posts = {}
    if nearest_titles:
        for title in nearest_titles:
            close_posts[title] = db[title]
    return json.dumps(close_posts)

app.run(host='0.0.0.0', port=8080)
