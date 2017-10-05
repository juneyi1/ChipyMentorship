from flask import Flask, url_for
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye World !"

@app.route("/hello")
def hello_name():
    args= request.args
    print(args)
    name = args['name']
    age = args['age']
  #  args['']
    #print(name) 
    return 'name is {} and age is {}'.format(name, age) 
    #return 'name is {}'.format(name)

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('goodbye'))
    print(url_for('hello_name'))
