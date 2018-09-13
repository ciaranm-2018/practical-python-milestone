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

    # Randomly select 5 of the riddles and convert the resulting array into a string.
    # We do this so that we can store the values using an input hidden form field.
    riddle_numbers = random.sample(range(0, 12), 5)
    riddle_numbers_string = str(riddle_numbers)
    riddle_numbers_string = riddle_numbers_string.replace('[','')
    riddle_numbers_string = riddle_numbers_string.replace(']','')
    riddle_numbers_string = riddle_numbers_string.replace(' ','')

    if request.method == "POST":
        # Get the riddles from a hidden field passed in form and convert from string to array.
        riddle_numbers_string = request.form["riddle_numbers_string"]
        riddle_numbers = map(int, riddle_numbers_string.split(','))
        
        # Get riddle index and score from hidden field passed in form.
        riddle_index = int(request.form["riddle_index"])
        score = int(request.form["score"])
        
        # Convert to lowercase, so correct answers will be accepted, regardless of case.
        user_response = request.form["message"].lower()

        # Compare the user's answer to the correct answer of the riddle
        if riddles[riddle_numbers[riddle_index]]["answer"] == user_response:
            score += 1
        
        # Progress to next riddle.    
        riddle_index += 1


# Check if the final riddle has been answered, if so, redirect to the result.html page/
    if riddle_index > 4:
        # Create message based on score.
        message = create_result_message(username, score)
        
        # Remove any commas from the username, as they will corrupt the file we are writing to.
        username = username.replace(',','')
        
        now = datetime.datetime.now()
        
        # Store the user's name, score and the current time in the results.txt file.
        #record = Record(username, str(score), str(now))
        record = username + ',' + str(score) + ',' + str(now) +'\n'
        filename='data/records.txt'
        write_to_file(filename, record)
     
        return render_template("result.html", **locals());
        
    riddle=riddles[riddle_numbers[riddle_index]]["description"]
    image_source = riddles[riddle_numbers[riddle_index]]["image_source"]
    alt_image_text = riddles[riddle_numbers[riddle_index]]["name"] 
        
    return render_template("game.html", username=username, riddle=riddle, image_source=image_source, 
    alt_image_text=alt_image_text, score=score, riddle_index=riddle_index, riddle_numbers_string=riddle_numbers_string)





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)