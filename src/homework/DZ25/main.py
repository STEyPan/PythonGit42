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
        return f"{self.__radius}"

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
        return Circle(self.__radius + other)

    def __sub__(self, other):
        return Circle(self.__radius - other)

    def __iadd__(self, other):
        self.__radius += other
        return self

    def __isub__(self, other):
        self.__radius -= other
        return self


circle_1 = Circle(2)
circle_2 = Circle(2)
print(circle_1.get_circumference())
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