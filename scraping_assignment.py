from bs4 import BeautifulSoup
import urllib.request

# Define the URL
url = 'http://py4e-data.dr-chuck.net/comments_1876994.html'

# Read the HTML content from the URL
with urllib.request.urlopen(url) as response:
    html_content = response.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the span tags with class "comments"
comments_tags = soup.find_all('span', class_='comments')

# Extract the numbers and sum them
total_sum = sum(int(tag.text) for tag in comments_tags)

print('Count:', len(comments_tags))
print('Sum:', total_sum)
