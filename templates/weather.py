import requests, json
from beautifulsoup4 import BeautifulSoup

soup = BeautifulSoup(open('home.html'))
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    text = text.replace('"', '')
    print(text)
  
loc = input('Location: ')
response = requests.get(
    'http://api.weatherapi.com/v1/current.json?key=01a5cccc8c004c2a88d222616220605&q='
    + loc + '&aqi=no')
weatherapi = response.json()
current = weatherapi.get('current')
tempf = current.get('temp_f')
tempc = current.get('temp_c')
isday = current.get('is_day')
#print(response.status_code)
print(tempf)

old = soup.find('span', {'id': 'weather'})
new = old.find(text=re.compile(‘’)).replace_with(tempf)
