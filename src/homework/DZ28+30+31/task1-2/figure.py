import abc

class Figure(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def __del__(self):
        pass

    @abc.abstractmethod
    def calc_area(self):
        pass

