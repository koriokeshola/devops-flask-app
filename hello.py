from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>This is another string!</p><p><a href="/about">About</a></p><p><a href="/contact">Contact</a></p>'

@app.route('/about')
def about():
	return '<p>This application is running on the Flash web framework.</p><p><a href="https://flask.palletsprojects.com">Flask Documentation</a></p>'

@app.route('/contact')
def contact():
	return '<p>My email address is: <a href="mailto:c23401212@mytudublin.ie">c23401212@mytudublin.ie</a></p>'


