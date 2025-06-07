class Complex:
    __complex_number = complex(0,0)

    def __init__(self, complex_number : complex = 0+0j):
        self.__complex_number = complex_number

    def __del__(self):
        pass

    def __str__(self):
        return f"{self.__complex_number}"

    def __add__(self, other): # +
        if isinstance(other, Complex):
            return Complex(self.__complex_number + other.__complex_number)
        elif isinstance(other, complex):
            return Complex(self.__complex_number + other)
        else:
            raise "Ошибка типов (TypeError)"

    def __sub__(self, other): # -
        if isinstance(other, Complex):
            return Complex(self.__complex_number - other.__complex_number)
        elif isinstance(other, complex):
            return Complex(self.__complex_number - other)
        else:
            raise "Ошибка типов (TypeError)"

    def __mul__(self, other): # *
        if isinstance(other, Complex):
            return Complex(self.__complex_number * other.__complex_number)
        elif isinstance(other, complex):
            return Complex(self.__complex_number * other)
        else:
            raise "Ошибка типов (TypeError)"

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__complex_number / other.__complex_number)
        elif isinstance(other, complex):
            return Complex(self.__complex_number / other)
        else:
            raise "Ошибка типов (TypeError)"



complex_num_1 = Complex(complex(2,2))
complex_num_2 = Complex(complex(2,-2))
print(complex_num_1)
print("-================================================-")
print("Сложение:")
print(complex_num_1 + complex_num_2)
print(complex_num_1 + (2-2j))
print("-================================================-")
print("Вычитание:")
print(complex_num_1 - complex_num_2)
print(complex_num_1 - (2-2j))
print("-================================================-")
print("Умножение:")
print(complex_num_1 * complex_num_2)
print(complex_num_1 * (2-2j))
print("-================================================-")
print("Деление:")
print(complex_num_1 / complex_num_2)
print(complex_num_1 / (2-2j))
print("-================================================-")