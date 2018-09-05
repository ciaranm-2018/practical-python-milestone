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
        
def write_to_file(filename, data):
    with open(filename, "a") as filehandle:
        filehandle.writelines(data)
        
        
def read_from_csv_file(filename):
    records = []
    with open(filename) as csvfile:
        for row in csv.reader(csvfile):
            name = row[0]
            score = int(row[1])
            date = parser.parse(row[2]).strftime('%d, %b %Y')
            records.append({'name': name, 'score': score, 'date': date})

    return records
    
    
def create_result_message(username, score):
    if (score == 5):
        message = "Well done " + username +", you got a perfect score (5/5)!"
    elif (score > 2):
        message = "Well done " + username +", you got (" + str(score) + "/5)."
    else:
        message = "Better luck next time " + username + ", you got (" + str(score) + "/5)."
        
    return message
    
# Generate a HTML table for the leaderboard.
def generate_html_table():
    # Declare your table
    class ItemTable(Table):
        name = Col('Name')
        score = Col('Score')
        date = Col('Date')
        classes = ['table']
        table_id = 'leaderboard_table'
 
    # Read records from file.
    records = read_from_csv_file('data/records.txt')
    
    # Sort records by score.
    records = sorted(records, key=lambda k: k['score'], reverse=True) 

    # Populate the table
    table = ItemTable(records)
    
    return table


# Process the homepage / riddles.html page. 
@app.route('/', methods=["GET", "POST"])
def index():
    
    # Handle POST request
    if request.method == "POST":
        return redirect(request.form["username"])
    return render_template("index.html")


# After entering a username the user is redirected to the game.html page. 
# This is handled here.
@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    # Import all of the riddles from the riddles.json file.
    riddles = []
    with open("data/riddles.json", "r") as json_data:
        riddles = json.load(json_data)
        
    riddle_index = 0
    score = 0;


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