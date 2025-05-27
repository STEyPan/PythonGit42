# class <Имя класса>:

class Person:
    # __name = "Jonh"
    #
    # def get_name(self):
    #     return self.__name

    def __init__(self, name = "Mike", age = 25):
        self.__name = name
        self.__age = age

    def __del__(self):
        pass

    # def set_name(self, new_name):
    #     self.__name = new_name
    # def get_name(self):
    #     return self.__name
    @property
    def name(self) -> str:
        return self.__name

    @name.setter # Сеттеры могут быть объявлены ТОЛЬКО после объявления свойств
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age: int):
        self.__age = new_age if new_age > 0 else 0


pers = Person(age=-100)
pers.age = -1200
print(pers.name)
print(pers.age)

