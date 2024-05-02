# Для пошуку та виведення всіх авторів працюємо за тим самим принципом — 
# спершу потрібно вручну вивчити сторінку. Можна звернути увагу на те, що 
# кожен автор взятий в тег <small> з класом author. 
# Далі використовуємо функцію find_all() та зберігаємо результат у змінній authors.

import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
quotes = soup.find_all("small", class_="author")

for quote in quotes:
    print(quote.text)
    