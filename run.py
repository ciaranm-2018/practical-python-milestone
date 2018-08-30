import csv, datetime, json, os, random
from dateutil import parser
from flask import flash, Flask, redirect, render_template, request
from flask_mail import Mail, Message
from flask_table import Table, Col
import urllib
import urllib2


app = Flask(__name__)
app.secret_key = 'some_secret'

mail_settings = {
    "MAIL_SERVER": 'smtp.mail.yahoo.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'c.mitch2018@yahoo.com',
    "MAIL_PASSWORD": 'Signup111'
}

app.config.update(mail_settings)
mail = Mail(app)

class Record(object):
    def __init__(self, name, score, date):
        self.name = name
        self.score = score
        self.date = date


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        flash("Thanks {}, enjoy the riddles".format(request.form["name"]))
    return render_template("index.html")


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_heading="Riddles", company=data)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]))
    return render_template("contact.html", page_heading="Contact")




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)