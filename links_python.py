from bs4 import BeautifulSoup
import urllib.request

# Prompt user for input
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Repeat the process 'count' times
for i in range(count):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all anchor tags
    anchors = soup('a')
    
    # Get the href attribute of the anchor tag at the specified position
    url = anchors[position - 1].get('href', None)

# Print the final URL retrieved
print('Retrieving:', url)

# Extract the name from the URL and print it
name = url.split('_')[-1].split('.')[0]
print('The answer to the assignment for this execution is "{}".'.format(name))
