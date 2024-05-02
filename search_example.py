import json
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all(attrs={"class": "quote"})

result_quotes = []

# quotes.a == quotes.find('a') == quotes.find_all('a')[0]
# quotes.find(class_="abc") == quotes.find(attrs={"class": "abc"})
# quotes.attrs["class"] == quotes["class"]
# quotes.text == quotes.get_text()

for quote in quotes:
    print(quote.text)

for quote in quotes:
    print(quote)
    result_quote = {
        "text": quote.find("span").text,
        "author": {
            "name": quote.find("small").text,
            "person_page": f"{url}{quote.find('a').attrs['href']}"
        },
        "tags": [
            { "name": item.text, "link": f"{url}{item['href']}" }
            for item in quote.find_all('a', attrs={'class': 'tag'})
            ]
    }

    meta_item = quote.find(attrs={"class": "keywords"})
    tags = meta_item.attrs["content"].split(",")

    print(result_quote)
    print(json.dumps(result_quote, indent=4))
    # exit(1)
