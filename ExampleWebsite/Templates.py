from flask import Flask, url_for
from flask import request
from flask import render_template
from jinja2 import Template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye World !"

@app.route('/hello/<username>')
def hello_user(username=None):
    # show the user profile for that user
    template = Template('Hello {{ name }}!')
    return template.render(name=username)

@app.route('/user/<username>')
def user(username=None):
    # show the user profile for that user
    return render_template('hello.html', name=username)
