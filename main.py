# -*- coding: cp1251 -*-

import requests

class Saller:
    def __init__(self, price, isNotEmpty):
        self.price = price
        self.isNotEmpty = isNotEmpty

class Auto:
    def __init__(self, manuf, code, automag, garage):
        self.manuf = manuf
        self.code = code
        self.automag = automag
        self.garage = garage

class Product:
    def __str__(self):
        return f"{self.maker} - {self.price}"

autos = [
    Auto("VAG", "N91096705", Saller(24.00, True), Saller(15.24, True)),
    Auto("VAG", "N91057001", Saller(26.40, True), Saller(14.46, True))
    ]

URL = "https://avto.pro/part-N91057001-LAMBORGHINI-681/"
# args = "?filter=9501%3D1196%3B"

import time, random

time.sleep(3 + random.random() * 4)
resp = requests.get(URL)
resp.encoding = "UTF8"
with open("index.html", "w") as f:
    f.write(resp.text)
# print(resp.text)

import bs4

soup = bs4.BeautifulSoup(resp.text, "html.parser")
table = soup.select("#js-partslist-primary > tbody > tr")
# print(table)
with open("price.log", "w"):...
for row in table:
    product = Product()
    product.maker = row.select('[data-type |= "maker"]')[0].text.replace("\n","").replace("\r","")
    product.maker = product.maker.strip()
    product.price = row.select('[data-type |= "price"]')[0].text.replace("\n","").replace("\r","")
    product.price = product.price.strip()
    print(product)
    with open("price.log", "a", encoding="utf") as f:
        f.write(product.__str__()+"\n")




# target="_blank"
