from flask import Flask, request, render_template
from replit import db
import difflib
import os
import json
import random
from datetime import datetime
from collections import OrderedDict
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config['ENV'] = 'production'
app.config['DEBUG'] = False
app.config['TESTING'] = False

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

delete_key = os.environ['DELETE_KEY']

def isNewTitle(key):
    if key in db.keys():
        return False
    else:
        return True


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        data = request.get_json(force=True)
        if data['body'] == delete_key:
            keys = db.keys()
            for key in keys:
                del db[key]
            print("cleared database!")
        elif not data['title'] in db.keys():
            data['likes'] = "0"
            data['date']= datetime.now().timestamp()
            db[data['title']] = data
            return "Added Successfully!"
        else:
            return "An error has occurred"
    return "hi bot"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/posts')
def posts():
    keys = db.keys()
    post_dict = {}
    for key in keys:
        try:
            post_dict[key] = db[key]
        except KeyError:
            continue
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


@app.route('/random')
def random_post():
    titles = list(db.keys())
    rand_title = random.choice(titles)
    return json.dumps(db[rand_title])

app.run(host='0.0.0.0', port=8080, threaded=True)
