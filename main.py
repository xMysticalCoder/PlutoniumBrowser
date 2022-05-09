#WEBSITE FORMAT = db["website:"+webname] = [password, data]
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import random, string
from flask import Flask, render_template, request, url_for
from replit import db
import random

f = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)


def resetWebsites():
    for i in db.prefix("website:"):
        p = db[i][0]
        d = db[i][1]
        del db[i]
        print(f"Deleted {i} with password {p} and data: {d}")
def resetAds():
  db["ads"] = []
  print("Reset all advertisements")

def resetAll():
  for i in db.prefix("website:"):
        p = db[i][0]
        d = db[i][1]
        del db[i]
        print(f"Deleted {i} with password {p} and data: {d}")
  db["ads"] = []
  print("Reset database")


def currentTime(city):
  geolocator = Nominatim(user_agent="geoapiExercises")

  lad = city
  location = geolocator.geocode(lad)
  obj = TimezoneFinder()

  # returns timezone
  result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
  print("Time Zone : ", result)

  tzinput = pytz.timezone(result)

  datetimeintz = datetime.now(tzinput)

  return datetimeintz.strftime("%H:%M:%S")
  





ok_chars = string.ascii_letters + string.digits
#resetAll()


@f.route('/')
def home():

    return render_template("home.html")


@f.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":

        website = request.form.get('url')
        if "website:" + website in db.prefix("website:"):
            data = db["website:" + website][1]
            
            print("Website")
        else:
            data = " Error 404 Website Not Found"
        ad = db["ads"][random.randint(0,len(db["ads"]))-1]
        return render_template('search.html', data=data, website=website, advertisement=ad)
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
        createwebpassword = request.form.get("createwebpassword")

        if createwebname.endswith(
                ".com") and "website:" + createwebname not in db.prefix(
                    "website:"):

            db["website:" + createwebname] = [createwebpassword, createwebdata]
            return render_template("createwebsuccess.html",
                                   website=createwebname,
                                   password=createwebpassword)

        else:
            if "website:" + createwebname in db.prefix("website:"):
                return render_template("createwebfailed2.html")
            else:
                return render_template("createwebfailed1.html")
    else:
        return render_template("createweb.html")


@f.route("/editweb", methods=['GET', 'POST'])
def editWeb():
    return render_template("editweb.html")


@f.route("/editwebverify", methods=["GET", "POST"])
def editWebVerify():
    if request.method == "POST":
        website = request.form.get("editwebname")
        data = request.form.get("editwebdata")
        password = request.form.get("editwebpassword")

        if "website:" + website in db.prefix("website:"):
            if password == db["website:" + website][0]:
                db["website:" + website] = [password, data]
                return render_template("editwebsuccess.html")
            else:
                return render_template("editwebfail2.html")
        else:
            return render_template("editwebfail1.html")

    else:
        return render_template("editweb.html")
@f.route("/signup", methods=["POST", "GET"])
def signup():
  return render_template("signup.html")

@f.route("/createad", methods=["POST", "GET"])
def createAd():
  return render_template("createad.html")
@f.route("/createadverify", methods=["POST", "GET"])
def createAdVerify():
  if request.method == "POST":
    adData = request.form.get("createaddata")
    if adData in db["ads"]:
      return render_template("createadfail1.html")
    else:
      db["ads"] = list(db["ads"]) + [adData]
      return render_template("createadsuccess.html", data=adData)
  else:
    return render_template("createad.html")

if __name__ == "__main__": 
    f.run(  
        host=
        '0.0.0.0',  
        port=random.randint(
            2000, 9000)  
    )
