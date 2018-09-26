from urllib.request import urlopen

from bs4 import BeautifulSoup

url = "https://treehouse-projects.github.io/horse-land/index.html"
html = urlopen(url)
soup = BeautifulSoup(html.read(), "html.parser")

print(soup.prettify())
