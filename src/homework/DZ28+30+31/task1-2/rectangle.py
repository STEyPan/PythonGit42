from figure import Figure

class Rectangle(Figure):
    __length = 0
    __width = 0

    def __init__(self,
                 length: int = 0,
                 width : int = 0):

        self.__length = length
        self.__width = width

    def __del__(self):
        pass

    def calc_area(self):
        return self.__length * self.__width

    def __str__(self):
        return (f"Прямоугольник:\n"
                f"Длина  (a) - {self.__length}\n"
                f"Ширина (b) - {self.__width}")

    def __int__(self):
        if isinstance(self.calc_area(), int) or self.calc_area() % 1 == 0:
            return int(self.calc_area())

        raise "Площадь прямоугольника не является типом int"

    def __float__(self):
        if isinstance(self.calc_area(), float):
            return self.calc_area()

        raise "Площадь прямоугольника не является типом - float"

rect = Rectangle(2,4)
print(rect)
print(int(rect))

