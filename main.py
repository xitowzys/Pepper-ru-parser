from filecmp import clear_cache
from turtle import title
from bs4 import BeautifulSoup 

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

number_discounts_all_span = soup.find("li", {"class": "js-subNavItem-search"}).find("span", {"class": "js-subNavItem-count"})

print(number_discounts_all_span.text)
