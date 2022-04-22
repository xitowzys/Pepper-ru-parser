from bs4 import BeautifulSoup

class Products_links_usecase():
    def __call__(self, soup: BeautifulSoup):
        products_links_usecase = soup.find_all("a", {"class": "cept-dealBtn"})

        for h in products_links_usecase:
            h_url = h.get("href")
            print(h_url)