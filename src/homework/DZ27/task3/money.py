import abc


class Money(abc.ABC):
    _whole = 0
    _cent = 0

    def __init__(self,
                 whole : int = 0,
                 cent : int = 0):

        if whole < 0:
            raise "Неверная запись данных (whole < 0)"

        else:
            self._whole = whole

        if cent > 99 or cent < 0:
            raise "Неверная запись данных (cent > 99 или cent < 0)"

        else:
            self._cent = cent

    def __del__(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        return f"{self._whole}: целая часть, {self._cent}: остаток"

    @abc.abstractmethod
    def __add__(self, other):
        if isinstance(other, Money):

            sum_whole = self._whole + other._whole
            sum_cent = self._cent + other._cent

            if sum_cent > 99:
                sum_whole += 1
                sum_cent %= 100

            return Money(sum_whole, sum_cent)

    @abc.abstractmethod
    def whole(self):
        return self._whole

    @property
    def whole(self):
        return self._whole

    @whole.setter
    def whole(self, new_whole : int = 0):
        if new_whole > 0:
            self._whole = new_whole
        else:
            raise "Неверная запись данных (whole < 0)"

    @abc.abstractmethod
    def cent(self):
        return self._cent

    @property
    def cent(self):
        return self._whole

    @cent.setter
    def cent(self, new_cent: int = 0):
        if new_cent > 0 and new_cent < 100:
            self._cent = new_cent
        else:
            raise "Неверная запись данных (cent > 99 или cent < 0)"
