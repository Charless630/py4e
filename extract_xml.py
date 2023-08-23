import urllib.request
import xml.etree.ElementTree as ET

# Prompt for URL
url = input("Enter location: ")
print("Retrieving", url)

# Read the XML data from the URL
with urllib.request.urlopen(url) as response:
    xml_data = response.read()
print("Retrieved", len(xml_data), "characters")

# Parse the XML data
tree = ET.fromstring(xml_data)

# Find all the 'count' tags using XPath
counts = tree.findall('.//count')

# Compute the sum of the numbers in the 'count' tags
total_sum = sum(int(count.text) for count in counts)

print("Count:", len(counts))
print("Sum:", total_sum)
