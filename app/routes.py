from app import app
from flask import render_template


@app.route('/')
def hello_world():
    return render_template('index.html', name = "Will")


@app.route('/favorite5sports')
def get_favorite_sports():
    sports = ["billiards", "basketball", "football", "American football", "boxing"]
    title = "Hello, my name is Will and here are my five favorite sports:"
    for i, sport in enumerate(sports, 1):
        title += f"\t{i}. {sport}"
    return title

@app.route('/test')
def favorite_five_test():
    return 'This is a test!!!'

from app import routes