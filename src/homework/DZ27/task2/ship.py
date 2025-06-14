import abc

class Ship(abc.ABC):
    _name = str()
    _country = str()
    _speed = 0.0
    _displacement = 0.0
    _armament = list()

    def __init__(self,
                 name : str = "Название",
                 country : str = "Страна",
                 speed : float = 0.0,
                 displacement : float = 0.0,
                 armament : list = []):

        self._name = name
        self._country = country
        self._speed = speed
        self._displacement = displacement
        self._armament = armament

    def __del__(self):
        pass

    @abc.abstractmethod
    def get_info(self):
        pass

    def start_engine(self):
        return f"Двигатель запущен"

    def stop_engine(self):
        return f"Двигатель выключен"

    def move_forward(self):
        return f"{self._name} двигается вперед"

    def move_back(self):
        return f"{self._name} двигается назад"

    def move_left(self):
        return f"{self._name} совершает поворот налево"

    def move_right(self):
        return f"{self._name} совершает поворот направо"





