#!/usr/bin/python
# coding=UTF-8
#
# Resolvr: A Wikidata Querying App
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

@app.route('/single_query', methods=['POST', 'GET'])
def single_query():
    errors = []
    if request.method == 'POST':
        # get IDs that the user has input
        try:
            id_entry = request.form['id_entry']
        except:
            errors.append('Sorry. Unable to get ID')
            return render_template("single_query.html", errors = errors)
        if id_entry:
            queryString = 'SELECT ?person ?personLabel WHERE { ?person wdt:P214 "' + id_entry + '" SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }}'
            try:
                




    return render_template("single_query.html", )

@app.route('/batch_query')
def batch_query(name=None):
    return render_template('batch_query.html', name=name)

@app.route('/data_view', methods=['POST'])
def data_view():
    file = request.files['data_file']
    if not file:
        return "No file"

    df = pd.read_csv(file)

    return df.to_html(classes='table table-striped')


if __name__ == '__main__':
    app.run(debug=True)
