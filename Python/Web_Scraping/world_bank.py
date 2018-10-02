from urllib.request import urlopen
from bs4 import BeautifulSoup

import csv


def get_country(country_code):
    url = "http://api.worldbank.org/v2/countries/{}".format(country_code)
    html = urlopen(url)
    soup = BeautifulSoup(html, "xml")
    country = soup.find("wb:name")
    region = soup.find("wb:region")
    income_level = soup.find("wb:incomeLevel")

    print(
        "\n*****\nCountry: {}, Region: {}, Income-level: {}\n*****\n".format(
            country.get_text(), region.get_text(), income_level.get_text()))


if __name__ == '__main__':
    file = open("country_iso_codes.csv", "r")
    iso_codes = csv.reader(file, delimiter=",")

    for code in iso_codes:
        get_country(code[0])
