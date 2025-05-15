# class <Имя класса>:

class Person:
    # __name = "Jonh"
    #
    # def get_name(self):
    #     return self.__name

    def __init__(self, name = "Mike"):
        self.__name = name
        print(f"Создан {self.__name}")

    def __del__(self):
        print(f"Удален {self.__name}")

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

