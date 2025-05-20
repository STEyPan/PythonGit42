
class Oper:
    __value = 0

    def __init__(self, value: int = 0):
        pass

    def __del__(self):
        pass

    def __bool__(self): # Оператор проверки на True/False
        return True if self.__value != 0 else False

    def __not__(self): # Оператор not
        return not self.__bool__()

    def __lt__(self, other): # Оператор меньше <
        if isinstance(other, Oper):
            return self.__value < other.__value
        elif isinstance(other, int):
            return self.__value < other
        else:
            return False

    def __le__(self, other): # Оператор меньше или равно <=
        if isinstance(other, Oper):
            return self.__value <= other.__value
        elif isinstance(other, int):
            return self.__value <= other
        else:
            return False

    def __gt__(self, other): # Оператор больше >
        if isinstance(other, Oper):
            return self.__value > other.__value
        elif isinstance(other, int):
            return self.__value > other
        else:
            return False

    def __ge__(self, other): # Оператор больше или равно >=
        if isinstance(other, Oper):
            return self.__value >= other.__value
        elif isinstance(other, int):
            return self.__value >= other
        else:
            return False

    def __ne__(self, other): # Оператор не равно !=
        return not (self == other)

    def __eq__(self, other): # Оператор равно ==
        if isinstance(other, Oper):
            return self.__value == other.__value
        elif isinstance(other, int):
            return self.__value == other
        else:
            return False


    def __abs__(self): # Оператор abs (абсолютное значение)
        return Oper(abs(self.__value))

    def __add__(self, other): # Оператор +
        if isinstance(other, Oper):
            return Oper(self.__value + other.__value)
        elif isinstance(other, int):
            return Oper(self.__value + other)
        else:
            raise "Ошибка типов"

    def __sub__(self, other): # Оператор -
        if isinstance(other, Oper):
            return Oper(self.__value - other.__value)
        elif isinstance(other, int):
            return Oper(self.__value - other)
        else:
            raise "Ошибка типов"

    def __mul__(self, other): # Оператор *
        if isinstance(other, Oper):
            return Oper(self.__value * other.__value)
        elif isinstance(other, int):
            return Oper(self.__value * other)
        else:
            raise "Ошибка типов"

    def __truediv__(self, other): # Оператор /
        if isinstance(other, Oper):
            return Oper(self.__value / other.__value)
        elif isinstance(other, int):
            return Oper(self.__value / other)
        else:
            raise "Ошибка типов"

    def __floordiv__(self, other): # Оператор //
        if isinstance(other, Oper):
            return Oper(self.__value // other.__value)
        elif isinstance(other, int):
            return Oper(self.__value // other)
        else:
            raise "Ошибка типов"

    def __pow__(self, power, modulo=None): # Оператор **
        return Oper(self.__value ** power)

    def __neg__(self): # Оператор математического отрицания
        return Oper(- self.__value)

    def __iadd__(self, other):  # Оператор +=
        if isinstance(other, Oper):
            self.__value += other
        elif isinstance(other, int):
            self.__value += other
        else:
            raise "Ошибка типов"

    def __isub__(self, other):  # Оператор -=
        if isinstance(other, Oper):
            self.__value -= other
        elif isinstance(other, int):
            self.__value -= other
        else:
            raise "Ошибка типов"

    def __imul__(self, other):  # Оператор *=
        if isinstance(other, Oper):
            self.__value *= other
        elif isinstance(other, int):
            self.__value *= other
        else:
            raise "Ошибка типов"

    def __itruediv__(self, other):  # Оператор /=
        if isinstance(other, Oper):
            self.__value /= other
        elif isinstance(other, int):
            self.__value /= other
        else:
            raise "Ошибка типов"

    def __ifloordiv__(self, other):  # Оператор //=
        if isinstance(other, Oper):
            self.__value //= other
        elif isinstance(other, int):
            self.__value //= other
        else:
            raise "Ошибка типов"

    def __ipow__(self, other):  # Оператор **=
        if isinstance(other, Oper):
            self.__value **= other
        elif isinstance(other, int):
            self.__value **= other
        else:
            raise "Ошибка типов"

    def is_(self, other):
        if isinstance(other, Oper):
            pass
        else:
            False

    def is_not(self, other):
        if isinstance(other, Oper):
            pass
        else:
            False

