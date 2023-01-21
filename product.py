
def format(value):
    return value.replace('\r', '').replace('\n', '').strip()

class Product:
    def __init__(self, maker = "", price = ""):
        self._maker = maker
        self._price = price

    def __str__(self):
        return f"{self._maker} - {self._price}"

    def __eq__(self, o):
        return self.maker == o.maker and self.price == o.price
        
    @property
    def maker(self):
        return self._maker

    @maker.setter
    def maker(self, value):
        self._maker = format(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = format(value)