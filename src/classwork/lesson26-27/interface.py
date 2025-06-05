import abc

class Interface(abc.ABC):
    def __init__(self):
        pass

    def __del__(self):
        pass

    @abc.abstractmethod
    def forward_moving(self):
        pass

    @abc.abstractmethod
    def backward_moving(self):
        pass

    @abc.abstractmethod
    def hand_brake(self):
        pass

    @abc.abstractmethod
    def start_engine(self):
        pass

    @staticmethod
    def static_method():
        pass