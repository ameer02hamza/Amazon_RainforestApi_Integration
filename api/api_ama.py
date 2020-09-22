import requests
import json
# set up the request parameters
params = {
  'api_key': 'demo',
  'type': 'category',
  'url': 'https://www.amazon.com/s?k=beauty&i=beauty-intl-ship&ref=nb_sb_noss'
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)
apic = json.loads(json.dumps(api_result.json()))
# print the JSON response from Rainforest API
print(apic['category_results'][1])

