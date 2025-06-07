class Circle:
    __radius = 0.0
    # __circumference = 2 * 3,14 * __radius

    def __init__(self, radius : float = 0.0):

        self.__radius = radius

    def __del__(self):
        pass

    def get_circumference(self):
        circumference = 2 * 3.14 * self.__radius
        return circumference

    def __str__(self):
        return (f"Радиус круга: {self.__radius}\n"
                f"Длина круга: {self.get_circumference()}")

    def __eq__(self, other): # ==
        if isinstance(other, Circle):
            return self.__radius == other.__radius
        else:
            return False

    def __gt__(self, other): # >
        if isinstance(other, Circle):
            return self.get_circumference() > other.get_circumference()
        else:
            return False

    def __ge__(self, other): # >=
        if isinstance(other, Circle):
            return self.get_circumference() >= other.get_circumference()
        else:
            return False

    def __lt__(self, other): # <
        if isinstance(other, Circle):
            return self.get_circumference() < other.get_circumference()
        else:
            return False

    def __le__(self, other): # <=
        if isinstance(other, Circle):
            return self.get_circumference() <= other.get_circumference()
        else:
            return False

    def __add__(self, other): # +
        if isinstance(other, (int, float)):
            return Circle(self.__radius + other)
        else:
            raise "Ошибка типов"

    def __sub__(self, other): # -
        if isinstance(other, (int, float)):
            return Circle(self.__radius - other)
        else:
            raise "Ошибка типов"

    def __iadd__(self, other): # +=
        if isinstance(other, (int, float)):
            self.__radius += other
            return self
        else:
            raise "Ошибка типов"

    def __isub__(self, other): # -=
        if isinstance(other, (int, float)):
            self.__radius -= other
            return self
        else:
            raise "Ошибка типов"


circle_1 = Circle(2)
circle_2 = Circle(3)
print(f"Длина circle_1: {circle_1.get_circumference()}")
print(f"Длина circle_2: {circle_2.get_circumference()}")
print(circle_1 == circle_2)
print(circle_1 == 2)
print(circle_1 <= circle_2)
print(circle_1 >= circle_2)
circle_1 = circle_1 + 1
print(circle_1)
circle_1 += 1
print(circle_1)
circle_1 -= 1
print(circle_1)