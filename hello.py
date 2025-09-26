from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Hello, World, I am a Flask app!</p><p><a href="/about">About</a></p>'

@app.route('/about')
def about():
	return '<p>This application is running on the Flash web framework.</p><p><a href="https://flask.palletsprojects.com"Flask Documentation</a></p>'

