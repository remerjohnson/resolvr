#!/usr/bin/python
# coding=UTF-8
#
# Resolvr Wikidata Querying App
#

import os
from flask import *
import pandas as pd
from werkzeug.utils import secure_filename
# Declare and load the app
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['csv', 'xsl', 'xslx'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home(name=None):
    return render_template('home.html', name=name)

@app.route('/query', methods=['GET', 'POST'])
def query(name=None):
    return render_template('query.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
