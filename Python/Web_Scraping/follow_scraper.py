from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

site_links = []


def internal_links(linkURl):
    url = "https://treehouse-projects.github.io/horse-land/{}".format(linkURl)
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "html.parser")

    return soup.find("a", href=re.compile('(.html)$'))


if __name__ == "__main__":
    urls = internal_links("index.html")
    while len(urls) > 0:
        page = urls.attrs["href"]
        if page not in site_links:
            site_links.append(page)
            print(page)
            print("\n=================\n")
            urls = internal_links(page)
        else:
            break