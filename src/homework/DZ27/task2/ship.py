import abc

class Ship(abc.ABC):
    _name = str()
    _corpus = str()
    _fuel_consumption = 0.0
    _speed = 0.0
    _displacement = 0.0

    def __init__(self,
                 name : str = "Название",
                 corpus : str = "Корпус",
                 fuel_consumption : float = 0.0,
                 speed : float = 0.0,
                 displacement : float = 0.0):

        self._name = name
        self._corpus = corpus
        self._fuel_consumption = fuel_consumption
        self._speed = speed
        self._displacement = displacement

    def __del__(self):
        pass




