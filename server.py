#!/usr/bin/env python3

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route("/")
def affTemp():
    return render_template('index.html')

app.run(debug=True, host='0.0.0.0', port=5000)