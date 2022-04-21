from cgitb import strong
from xml import dom
import domain.usecase

from filecmp import clear_cache
from re import T
from turtle import title
from bs4 import BeautifulSoup



with open("index.html", "r") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

get_number_discounts_usecase = domain.usecase.Get_number_discounts_usecase()
number_discounts_all_span = get_number_discounts_usecase(soup)

print(number_discounts_all_span)

products_all_article = soup.find_all("article", {"class": "thread--deal"})
print(type(products_all_article))

for i, article in enumerate(products_all_article):
    if 'thread--expired' in article.attrs['class']: 
        # products_all_article.pop(i)
        article.decompose()

    else:
        continue

print(len(products_all_article))


for t in products_all_article:
    if not t.decomposed:
        print(t.find("a",class_ = "thread-title--list").get('title', 'No title attribute'))
