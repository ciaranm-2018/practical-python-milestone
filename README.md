 -Overview-
  
  Harry Potter Riddles

This is a website designed for fans of Harry Potter, who wish to 
test their knowledge of Harry Potter by completing a set of riddles
based on the Harry Potter books.

It demonstrates the use of HTML, CSS, jS, Python, Bootstrap and Font Awesome.


 -Features-
 
Users are prompted to enter a username before starting the riddles.
Each user is presented with five riddles, selected from a possible twelve, 
which are stored in the riddles.json file.

When the user has answered all of the questions, they receive a final
score, and their name and score is recorded on the leaderboard.
A record of the users and their scores is contained in records.txt.

Users are also allowed to suggest their own riddles to be included in the site.
They can do this via the contact page. All messages will be sent to my
personal email address. I have currently set up the page so that the sender's address
defaults to my address also, but it can be set up to work with any email address.

 -Testing-

Go to riddles page. Enter a username to progress. Ensure that riddles don't load unless
a username is entered. The user will be brought back to the login page.

Once logged in, ensure that the 'enter' button will bring the user to the next riddle.
Ensure that 'Well done {{username}} you got a perfect score (5/5)!' is returned when the
user obtains a score of 5/5. 
Ensure that 'Better luck next time, you got ( /5)' is returned
if the user obtains a score of less than 5.

Ensure that the user's username and score are recorded on the leaderboard in numerical order.
This data is stored in records.txt.

Ensure that 'please fill out this field' is returned when the user fails to input a name,
e-mail address or message.

Ensure that email addresses will not be accepted without the '@' character.

Ensure that 'Thanks, your message has been sent!' is returned when a user 
successfully submits a message.

Ensure that the 'Harry Potter Riddles' logo returns the user to the home page.
 


 
 -Deployment-

 This site has been deployed at https://hp-riddles.herokuapp.com/
 


-Credits-
 
 Content:
 
 The content used in this site was obtained from: http://www.funtrivia.com
 
 Media:
 
 The photos used in this site were obtained from: https://upload.wikimedia.org
                                                  https://c1.staticflickr.com/
                                                  

 -Author-

 Ciaran Mitchell
 