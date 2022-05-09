
import requests
          
url = "https://api.uptimerobot.com/v2/getMonitors"
          
payload = "api_key=m790917851-22d88f6ccdae631852b8c5a9&format=json&logs=1"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }
          
response = requests.request("POST", url, data=payload, headers=headers)
answer = response.json()
stats = answer.get('stat')
if stats == 'ok':
  print('Server is running!')
  server = 'ok'
else:
  print('Server may be down, or we may be out of calls to check. Try again later.')
  server = 'unknown'
