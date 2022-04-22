from bs4 import BeautifulSoup

class Products_price_usecase():
    def __call__(self, soup: BeautifulSoup):
        product_price_all = soup.find_all("span", {"class": "thread-price"})

        for y in product_price_all:
            print(y.text) #не выводит последнее число