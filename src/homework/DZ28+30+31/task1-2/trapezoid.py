from figure import Figure

class Trapezoid(Figure):
    __side_a = 0
    __side_b = 0
    __height = 0

    def __init__(self,
                 side_a : int = 0,
                 side_b : int = 0,
                 height : int = 0):

        self.__side_a = side_a
        self.__side_b = side_b
        self.__height = height

    def __del__(self):
        pass

    def calc_area(self):
        return (self.__side_a + self.__side_b) / 2 * self.__height

    def __str__(self):
        return (f"Трапеция:\n"
                f"Сторона (a) - {self.__side_a}\n"
                f"Сторона (b) - {self.__side_b}\n"
                f"Высота (h) - {self.__height}")

    def __int__(self):
        if isinstance(self.calc_area(), int) or self.calc_area() % 1 == 0:
            return int(self.calc_area())

        raise "Площадь трапеции не является типом - int"

    def __float__(self):
        if isinstance(self.calc_area(), float):
            return self.calc_area()

        raise "Площадь трапеции не является типом - float"


trapezoid = Trapezoid(3,4,5)
print(trapezoid)
print(float(trapezoid))