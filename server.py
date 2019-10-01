# run with
#FLASK_APP=server.py FLASK_DEBUG=1 python -m flask run

from flask import Flask, redirect, url_for
import flask

import pandas as pd

compliants = pd.read_csv('./data/credit_card_complaint_types_subset.csv')

app = Flask(__name__)
app.secret_key = "Shhhhhh"


@app.route("/")
def homepage():

    htmldata = compliants[['Product', 'Issue', 'Consumer complaint narrative', 'Complaint ID']].to_html()

    return flask.render_template('index.html',render_data=htmldata)

@app.route('/case/<id>')
def profile(id):
    dat = compliants.loc[int(id)].to_dict()
    lda_topic_colour=dict()
    for i in range(0,8):
        lda_topic_colour[i]=None
    lda_topic_colour[dat['most_likely']]='red'
    return flask.render_template('case.html', dat=dat,lda_topic_colour=lda_topic_colour)


if __name__ == "__main__":
    app.run()
