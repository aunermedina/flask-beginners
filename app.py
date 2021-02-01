#!python3

from flask import Flask, request, render_template

# setting up flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rootpage():
    name = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        
    return render_template("index.html", name=name)


app.run()