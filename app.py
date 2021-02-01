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

@app.route('/bmi-calc', methods=['GET', 'POST'])
def bmicalc():
    weight = ''
    height = ''
    result = ''
    if request.method == 'POST' and 'weight' and 'height' in request.form:
        weight = request.form.get('weight')
        height = request.form.get('height')
        result = float(weight) / pow(float(height), 2)
    
    return render_template("bmi_calc.html", result=result)
    

app.run()