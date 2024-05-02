# Для отримання лише даних - цитат у цьому випадку, можна використовувати властивість .text.
import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
quotes = soup.find_all("span", class_="text")

for quote in quotes:
    print(quote.text)
    