import urllib.request
import urllib.parse
import json

# API endpoint
service_url = 'http://py4e-data.dr-chuck.net/json?'

# Prompt for the location
address = input('Enter location: ')

# Prepare the URL with the address and key parameters
params = {
    'address': address,
    'key': 42
}
url = service_url + urllib.parse.urlencode(params)

print('Retrieving', url)

# Open the URL and read the data
with urllib.request.urlopen(url) as response:
    data = response.read().decode()
    print('Retrieved', len(data), 'characters')

# Parse the JSON data
parsed_json = json.loads(data)

# Retrieve the first place_id
place_id = parsed_json['results'][0]['place_id']
print('Place id', place_id)
