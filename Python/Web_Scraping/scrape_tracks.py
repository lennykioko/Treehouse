from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://teamtreehouse.com/tracks/learn-react"
html = urlopen(url)
soup = BeautifulSoup(html.read(), "html.parser")

course_title = soup.find("h2").get_text()
course_duration = soup.find("span", {
    "class": "estimate add-topic-background-color"
}).get_text()
course_description = soup.find("div", {"id": "track-meta"}).p.get_text()

print("\n")

print("{} ({}).\n".format(course_title.upper(), course_duration.strip()))

print(course_description)
print("\n{} MODULES.\n".format(course_title.upper()))

course_modules = soup.find_all("h3", {"class": "card-title"})
module_durations = soup.find_all("span", {"class": "card-estimate"})

for (course_module, module_duration) in zip(course_modules, module_durations):
    print("{} ({}).".format(course_module.get_text(),
                            module_duration.get_text()))

print("\n")
