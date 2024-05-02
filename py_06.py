# Пошук елементів

import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# знайти перший тег <p> на сторінці
print("-------------------------------")
first_paragraph = soup.find("p")
print(first_paragraph)

# отримати текст першого тега <p> на сторінці
print("-------------------------------")
first_paragraph_text = first_paragraph.get_text()
print(first_paragraph_text.strip()) # "Login"

# отримати значення атрибута "href" першого тегу <a> на сторінці
print("-------------------------------")
first_link = soup.find("a")
first_link_href = first_link["href"]
print(first_link_href) # "/"



# знайти всі теги <p> на сторінці
print("-------------------------------")
all_paragraphs = soup.find_all("p")
print(all_paragraphs)

# отримати текст всі теги <p> на сторінці
print("-------------------------------")
for paragraph in all_paragraphs:
    paragraph_text = paragraph.get_text()
    print(paragraph_text.strip())

# отримати значення атрибута "href" всі теги <a> на сторінці
print("-------------------------------")
all_links = soup.find_all("a")
for link in all_links:
    link_href = link["href"]
    print(link_href)

