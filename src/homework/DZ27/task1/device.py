import abc


class Device(abc.ABC):
    _name = str()
    _fabricator = str()
    _color = str()
    _price = 0.0
    _switch = False


    def __init__(self,
                 name : str = "Название",
                 fabricator : str = "Производитель",
                 color : str = "Цвет",
                 price : float = 0.0):

        self._name = name
        self._fabricator = fabricator
        self._price = price

    def __del__(self):
        pass

    @abc.abstractmethod
    def price(self):
        return self._price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price : float = None):
        if new_price != None and new_price > 0:
            self._price = new_price

    @abc.abstractmethod
    def color(self):
        return self._color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color: str = None):
        if new_color != None:
            self._color = new_color

    @abc.abstractmethod
    def switch(self):
        return self._switch

    @property
    def switch(self):
        return self._switch

    @switch.setter
    def switch(self, new_switch : bool = False):
        if new_switch:
            self._switch = True
            return self._switch

        self._switch = False
        return self._switch


    def device_status(self):
        if self.switch:
            return f"{self._name} включен"

        return f"{self._name} выключен"

    def get_data(self):
        return (f"Название: {self._name}\n"
                f"Производитель: {self._fabricator}\n"
                f"Цена: {self._price:,} рублей")


