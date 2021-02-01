#!python3

from flask import Flask, request

# setting up flask app
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'this is my first flask app! Yay!'


@app.route('/potato')
def potatopage():
    return 'this is my potato flask page! Yay!'

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return "You've used a POST request!"
    else:
        return "I reckon you're probably using a GET request"

app.run()