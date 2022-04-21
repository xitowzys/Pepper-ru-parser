from bs4 import BeautifulSoup

class Get_number_discounts_usecase():
    def __call__(self, soup: BeautifulSoup):
        number_discounts_all_span = soup.find("li", {"class": "js-subNavItem-search"}).find("span", {"class": "js-subNavItem-count"})
        return number_discounts_all_span.text