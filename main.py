from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/blog/<user>')

def blog(user):
    stupid = ['stupid1', 'cantbelieve', 'seems imposible']
    return render_template('blog.html', userserv=user, stupid=stupid)