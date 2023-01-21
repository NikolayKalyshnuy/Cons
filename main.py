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

autos = [
    Auto("VAG", "N91096705", Saller(24.00, True), Saller(15.24, True)),
    Auto("VAG", "N91057001", Saller(26,40, True), Saller(14,46, True))
    ]

URL = "https://www.foxtrot.com.ua/ru/shop/dnepr/noutbuki_lenovo_diagonal-displeja-13-inches.html"
# args = "?filter=9501%3D1196%3B"

resp = requests.get(URL, params = {"filter" : r"9501%3D1196%3B", "sdfg" : "safghd"})
print(resp.request.url)