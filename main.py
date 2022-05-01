
import random, string
from flask import Flask, render_template, request
from replit import db
f = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
db["google.com"] = "testing lol 123"
ok_chars = string.ascii_letters + string.digits

@f.route('/')
def home():

  return render_template("home.html")

@f.route('/search', methods=['GET', 'POST'])
def search():
  website = request.form.get('url')
  if website in db.keys():
    data = db[website]
  else:
    data = "404 Website Not Found"
  return render_template('search.html', data=data, website=website)

if __name__ == "__main__":  # Makes sure this is the main process
	f.run( # Starts the site
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)
