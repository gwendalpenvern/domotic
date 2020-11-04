#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def affTemp():
    return render_template('index.html')#, temp=get_temperature(True), humi=get_humidity())

app.run(debug=True, host='0.0.0.0', port=5000)