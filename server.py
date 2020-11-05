#!/usr/bin/env python3

from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route("/")
def affTemp():
    return render_template('index.html', path_image="/static/images/" + str(datetime.datetime.now())[:10] + ".png" )

app.run(debug=True, host='0.0.0.0', port=5000)