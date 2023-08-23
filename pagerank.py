from bs4 import BeautifulSoup
import requests

def spider(url, max_pages=100):
    pages_to_visit = [url]
    visited_pages = set()
    links = {}

    while pages_to_visit and len(visited_pages) < max_pages:
        current_url = pages_to_visit.pop(0)
        if current_url not in visited_pages:
            response = requests.get(current_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            visited_pages.add(current_url)
            links[current_url] = []
            for link in soup.find_all('a'):
                link_url = link.get('href')
                if link_url and link_url.startswith('http'):
                    pages_to_visit.append(link_url)
                    links[current_url].append(link_url)

    return links

links = spider('http://python-data.dr-chuck.net/')

