#!/bin/bash
# Exit if command fails
set -e

# Update and upgrade Ubuntu without needing confirmation
sudo apt update -y
sudo DEBIAN_FRONTEND=noninteractive apt upgrade -y

# Install packages
sudo DEBIAN_FRONTEND=noninteractive apt install -y nano vim python-is-python3 python3-venv python3-pip

# Create virtual environment
python -m venv ~/.my_venv

# Activate virtual environment
source ~/.my_venv/bin/activate

# Install Flask
pip install flask

# Create Flask app
cat > ~/hello.py << 'EOF'
from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Hello, World, I am a Flask app!</p><p><a href="/about">About</a></p>'

@app.route('/about')
def about():
	return '<p>This application is running on the Flask web framework.</p><p><a href="https://flask.palletsprojects.com">Flask Documentation</a></p>'

EOF

# Start Flask
flask --app hello run --host 0.0.0.0

