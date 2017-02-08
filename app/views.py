from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
