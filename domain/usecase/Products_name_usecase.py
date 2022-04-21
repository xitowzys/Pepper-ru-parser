from unittest import result
from bs4 import BeautifulSoup

class Products_name_usecase():
    def __call__(self, soup: BeautifulSoup):
        result = []
        products_name_all_article = soup.find_all("article", {"class": "thread--deal"})
        
        for i, article in enumerate(products_name_all_article):
            if 'thread--expired' in article.attrs['class']:
                article.decompose()

            else:
                continue

        for t in products_name_all_article:
            if not t.decomposed:
                result.append(t.find("a",class_ = "thread-title--list").get('title', 'No title attribute'))
        
        return result
