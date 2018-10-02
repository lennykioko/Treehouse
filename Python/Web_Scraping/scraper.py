from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://treehouse-projects.github.io/horse-land/index.html"
html = urlopen(url)
soup = BeautifulSoup(html.read(), "html.parser")

# print(soup.prettify())

# divs = soup.find_all("div")
# for div in divs:
#     print(div)

# featured_div = soup.find("div", {"class": "featured"})
# print(featured_div)

# featured_header = soup.find("div", {"class": "featured"}).h2
# print(featured_header.get_text())

# buttons = soup.find(attrs={"class": "button button--primary"})
# for button in buttons:
#     print(button)

# buttons = soup.find(class_="button button--primary")
# for button in buttons:
#     print(button)

links = soup.find_all("a")
for link in links:
    print(link.get("href"))
