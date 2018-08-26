import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'some_secret'


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