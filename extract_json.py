import urllib.request
import json

# Prompt for the URL
url = input("Enter location: ")
print("Retrieving", url)

# Open the URL and read the data
with urllib.request.urlopen(url) as response:
    data = response.read().decode()
    print("Retrieved", len(data), "characters")

# Parse the JSON data
parsed_json = json.loads(data)

# Extract the comment counts and compute the sum
total_count = 0
for comment in parsed_json['comments']:
    total_count += comment['count']

print("Count:", len(parsed_json['comments']))
print("Sum:", total_count)
