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

products_name_usecase = domain.usecase.Products_name_usecase()
products_name = products_name_usecase(soup)

for i in products_name:
    print(i)

products_price_usecase = domain.usecase.Products_price_usecase()
products_price = products_price_usecase(soup)
print(products_price)
