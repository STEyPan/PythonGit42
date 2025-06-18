from figure import Figure

class RightTriangle(Figure):
    __side_a = 0
    __side_b = 0
    __hypotenuse = 0

    def __init__(self,
                 side_a : int = 0,
                 side_b : int = 0):

        self.__side_a = side_a
        self.__side_b = side_b

        hypotenuse = ((side_a ** 2) + (side_b ** 2)) ** (1/2)

        self.__hypotenuse = int(hypotenuse) if hypotenuse % 1 == 0 else hypotenuse

    def __del__(self):
        super().__del__()

    def calc_area(self):
        return (self.__side_a * self.__side_b) / 2

    def __str__(self):
        return (f"Прямоугольный треугольник:\n"
                f"Катет (a) - {self.__side_a}\n"
                f"Катет (b) - {self.__side_b}\n"
                f"Гипотенуза (с) - {self.__hypotenuse}")

    def __int__(self):
        if isinstance(self.calc_area(), int) or self.calc_area() % 1 == 0:
            return int(self.calc_area())

        else:
            raise "Площадь прямоугольного треугольника не является типом - int"

    def __float__(self):
        if isinstance(self.calc_area(), float):
            return self.calc_area()

        raise "Площадь прямоугольного треугольника не является типом - float"



rightTri = RightTriangle(4,3)
print(rightTri)
print(float(rightTri))