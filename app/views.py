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
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
