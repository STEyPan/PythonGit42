#
# Задание - На завод по производству автомобилей необходимо создать систему
# классов для ведения базы данных всех выпущенных авто.
# Авто обладают следующими характеристиками:
# 1) Цена
# 2) Название
# 3) Цвет
# 4) Мощность двигателя
# 5) Макс. скорость
# Необходимо реализовать классы для следующих видов машин:
# - Седан
#  1. АКПП/МКПП
#  2. Кол-во дополнительных опций
# - Внедорожник
#  1. Рамный или нет
#  2. Полный привод или нет
#  3. Блокировка
#  4. Вид топлива
#  - Грузовой
#  1. Тоннаж
#  2. Возможность установки прицепа
#  3. Наличие спального места
#  4. Кол-во мест

from interface import Interface
import abc

class Automobile(Interface):
    _name = str()
    _color = str()
    _power_engine = 0.0
    _price = 0.0
    _max_speed = 0

    def __init__(self,
                 name : str = "Название",
                 color: str = "Цвет",
                 power_engine : float = 0.0,
                 price: float = 0.0,
                 max_speed : int = 0):

        self._name = name
        self._color = color
        self._power_engine = power_engine
        self._price = price
        self._max_speed = max_speed

    def __del__(self):
        pass

    @abc.abstractmethod
    def forward_moving(self):
        return f"едет вперёд"

    @abc.abstractmethod
    def backward_moving(self):
        return f"едет назад"

    @abc.abstractmethod
    def hand_brake(self):
        return f"тормозит"

    @abc.abstractmethod
    def start_engine(self):
        return f"Двигатель заводится"

    @abc.abstractmethod
    def name(self):
        return self._name

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, new_name: str = None):
    #     if new_name != None:
    #         self._name = new_name
    #
    #     if isinstance(new_name, str):
    #         self._name = new_name
    #     else:
    #         raise "Ошибка типов"

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

        if isinstance(new_color, str):
            self._name = new_color
        else:
            raise "Ошибка типов"

    @abc.abstractmethod
    def power_engine(self):
        return self._power_engine

    @property
    def power_engine(self):
        return self._power_engine

    # @power_engine.setter
    # def power_engine(self, new_power_engine: float = None):
    #     if new_power_engine != None:
    #         self._power_engine = new_power_engine
    #
    #     if isinstance(new_power_engine, float):
    #         self._name = new_power_engine
    #     else:
    #         raise "Ошибка типов"

    @abc.abstractmethod
    def price(self):
        return self._price

    @property
    def price(self):
        return self._price

    # @price.setter
    # def price(self, new_price: float = None):
    #     if new_price != None:
    #         self._price = new_price
    #
    #     if isinstance(new_price, float):
    #         self._name = new_price
    #     else:
    #         raise "Ошибка типов"

    @abc.abstractmethod
    def max_speed(self):
        return self._max_speed
    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, new_max_speed: int = None):
        if new_max_speed != None:
            self._max_speed = new_max_speed

        if isinstance(new_max_speed, int):
            self._name = new_max_speed
        else:
            raise "Ошибка типов"

    @abc.abstractmethod
    def get_info(self):
        return (f"Название автомобиля: {self._name}\n"
                f"Цвет: {self._color}\n"
                f"Мощность двигателя: {self._power_engine} л.с.\n"
                f"Цена: {self._price:,} р.\n"
                f"Максимальная скорость: {self._max_speed} км/ч")


