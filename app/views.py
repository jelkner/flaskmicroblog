from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'Amanuel'},
            'body': "It's a beautiful day in the neighborhood!"
        },
        {
            'author': {'nickname': 'Marisol'},
            'body': "I hope we get a snow day before Winter ends!"
        },
        {
            'author': {'nickname': 'Rebecca'},
            'body': 'Dreamers still dreaming in the age of Trump!'
        },
        {
            'author': {'nickname': 'Elijshia'},
            'body': 'The struggle continues!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)
