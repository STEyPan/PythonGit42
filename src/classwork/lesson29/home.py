import abc

class Home(abc.ABC):
    _area = 0.0
    _input_power = 0.0

    def __init__(self,
                 area : float = 0.0,
                 input_power : float = 0.0):

        self._area = area
        self._input_power = input_power

    def __del__(self):
        pass

    @abc.abstractmethod
    def total_cost(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass
