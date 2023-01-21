import re

class Product:
    def __init__(self, maker = "", price = ""):
        self._maker = maker
        self._price = price

    def __str__(self):
        return f"{self._maker} - {self._price}"
        
    @property
    def maker(self):
        return self._maker

    @maker.setter
    def maker(self, value):
        self._maker = re.sub(r"[^\W ", "", value).strip()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = re.sub(r"[^\W ", "", value).strip()



