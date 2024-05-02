# Навігація документом. 
import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# знайти перший тег <p> на сторінці
print("-------------------------------")
first_paragraph = soup.find("p")
print(first_paragraph)

##################################
# Дочірні елементи
print("-------------------------------")
body_children = list(first_paragraph.children)
print(body_children)
# знайти перший тег <a> всередині першого тегу <div> на сторінці. ланцюжки методів find
print("-------------------------------")
first_div = soup.find("div")
first_div_link = first_div.find("a")
print(first_div_link)

####################################
# Батьківські елементи
print("-------------------------------")
first_paragraph_parent = first_paragraph.parent
print(first_paragraph_parent)
# методи find_parent і find_parents для пошуку батьківських елементів:
print("-------------------------------")
container = soup.find("div", attrs={"class": "quote"}).find_parent("div", class_="col-md-8")
print(container)

####################################
# Сусідні елементи
# отримати наступний сусідній елемент першого тегу <span> з класом "tag-item" на сторінці:
print("-------------------------------")
next_sibling = soup.find("span", attrs={"class": "tag-item"}).find_next_sibling("span")
print(next_sibling)
# отримати попередній сусідній елемент першого тегу <span> з класом "tag-item" на сторінці:
print("-------------------------------")
previous_sibling = next_sibling.find_previous_sibling("span")
print(previous_sibling)


