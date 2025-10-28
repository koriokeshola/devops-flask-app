from flask import Flask
import redis
import time

app = Flask(__name__)
r =  redis.Redis(host='redis-server', port=6379, decode_responses=True)

@app.route('/')
def say_hello():
	data = r.hgetall('say_hello')
	if data is not None:
		# 600 seconds == 10 minutes
		if time.time() - float(data.get('time', 0)) > 600:
			return data.get('html', '')
	data='<p>This is another string!</p><p><a href="/about">About</a></p><p><a href="/contact">Contact</a></p>'
	r.hset('say_hello', mapping={'html': data, 'time': time.time()})
	return data

@app.route('/about')
def about():
	data = r.hgetall('about')
	if data is not None:
		# 600 seconds == 10 minutes
		if time.time() - float(data.get('time', 0)) > 600:
			return data.get('html', '')
	data ='<p>This application is running on the Flash web framework.</p><p><a href="https://flask.palletsprojects.com">Flask Documentation</a></p>'
	r.hset('about', mapping={'html': data, 'time': time.time()})
	return data

@app.route('/contact')
def contact():
	data = r.hgetall('contact')
	if data is not None:
		# 600 seconds == 10 minutes
		if time.time() - float(data.get('time', 0)) > 600:
			return data.get('html', '')
	data ='<p>My email address is: <a href="mailto:C23401212@mytudublin.ie">C23401212@mytudublin.ie</a></p>'
	r.hset('contact', mapping={'html': data, 'time': time.time()})
	return data

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5001)
