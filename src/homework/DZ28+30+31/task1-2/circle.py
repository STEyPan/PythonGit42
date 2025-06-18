from figure import Figure

class Circle(Figure):
    __radius = 0

    def __init__(self, radius : int = 0):
        self.__radius = radius

    def __del__(self):
        pass

    def calc_area(self):
        return 3.14 * (self.__radius ** 2)

    def __str__(self):
        return (f"Круг:\n"
                f"Радиус - {self.__radius}\n"
                f"Диаметр - {self.__radius*2}")

    def __int__(self):
        if isinstance(self.calc_area(), int) or self.calc_area() % 1 == 0:
            return self.calc_area()

        raise "Площадь круга не является типом - int"


    def __float__(self):
        if isinstance(self.calc_area(), float):
            return self.calc_area()

        raise "Площадь круга не является типом - float"



circle = Circle(4)
print(circle)
print(float(circle))

