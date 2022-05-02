
import random, string
from flask import Flask, render_template, request, url_for
from replit import db
f = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

db["google.com"] = "testing lol 123"
del db["google.com"]
ok_chars = string.ascii_letters + string.digits

@f.route('/')
def home():

  return render_template("home.html")

@f.route('/search', methods=['GET', 'POST'])
def search():
  if request.method == "POST":
    
  
    website = request.form.get('url')
    if website in db.keys():
      data = db[website]
      print("Website")
    else:
      data = "404 Website Not Found"
    return render_template('search.html', data=data, website=website)
  else:
    return render_template("home.html")

@f.route("/createweb", methods=['GET', 'POST'])
def createWeb():
  return render_template("createweb.html")


@f.route("/createwebverify", methods=['GET', 'POST'])
def createWebVerify():
  if request.method == "POST":
    createwebname = request.form.get("createwebname")
    createwebdata = request.form.get("createwebdata")
    if createwebname.endswith(".com") and createwebname not in db.keys():
      return render_template("createwebsuccess.html", website = createwebname)
      
    else:
      if createwebname in db.keys():
        return render_template("createwebfailed2.html")
      else:
        return render_template("createwebfailed1.html")
  else:
    return render_template("createweb.html")



if __name__ == "__main__":  # Makes sure this is the main process
	f.run( # Starts the site
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)
