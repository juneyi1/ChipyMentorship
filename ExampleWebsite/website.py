from flask import Flask
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
