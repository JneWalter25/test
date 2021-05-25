import requests
import json
import re
from bs4 import BeautifulSoup
request = input("Input the URL:")

r = requests.get(f'{request}')
soup = BeautifulSoup(r.content, 'html.parser')
#print(r.status_code)
#print(r.json())
#print(json_dict)


movie = soup.find('meta', property='og:type', content=re.compile("video"))

if not movie or 'imdb' not in request:
    print("\nInvalid movie page!")
else:
    title = soup.find('title')
    desc = soup.find("meta", property="og:description")
    movie_dict = {
        "title": title.text,
        "description": desc.get('content')
    }
    print(movie_dict)