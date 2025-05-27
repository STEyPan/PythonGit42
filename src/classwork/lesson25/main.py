# Роли в Университете

# Студены - ФИО, Возраст, Группа
# Преподаватели - ФИО, Возраст, Кафедра
# Администрация - ФИО, Возраст, Должность

# Наследование - это возможность создания новой сущности (класса)
# на базе уже существующей сущности (другого класса)
# Наследование - это механизм языка, позволяющий передать механизмы
# от classA (родительский/superclass) в classB (наследник)

# Public: age - доступен всем
# protected: _age - только внутри родительского и дочернего класса
# private: __age - только внутри класса

# from typing import final
# @final - делает класс ненаследуемым

class Person:
    __name = str()
    __age = 0

    def __init__(self, name : str = "",
                       age : int = 0):
        self.__name = name
        self.__age = age

    def __del__(self):
        pass

    def __str__(self):
        return f"Имя {self.__name}\nВозраст: {self.__age}"

    def say_hello(self):
        return f"Привет, моё имя {self.__name}"

# Класс Student наследуется от класса Person
class Student(Person):
    __group = str()

    def __init__(self, name : str = "",
                       age : int = 0,
                       group : str = ""):
        super().__init__(name, age)
        self.__group = group

    def __del__(self):
        pass

    def say_hello(self): # Переопределение метода родителя
        return f"{super().say_hello()}. {self.__group}"

    def __str__(self):
        return f"{super().__str__()}\nГруппа: {self.__group}"

    def my_group(self):
        return f"Я из группы {self.__group}"

class Teacher(Person):
    __department = str()

    def __init__(self, name : str = "",
                       age : int = 0,
                       departament : str = ""):
        super().__init__(name, age)
        self.__department = departament

    def __del__(self):
        pass

    def my_departament(self):
        return f"Я с кафедры {self.__department}"

class Administration(Person):
    __post = str()

    def __init__(self, name : str = "",
                       age : int = 0,
                       post : str = ""):
        super().__init__(name, age)
        self.__post = post

    def __del__(self):
        pass

    def my_post(self):
        return f"Моя должность {self.__post}"

def func(obj: Person):
    print(obj.say_hello())


pers = Person("Христофор", 35)
print(pers.say_hello())
print("-============================-")

stud = Student("Наташа", 25, "Py42")
print(stud)
print(stud.my_group())
print(stud.say_hello())
print("-============================-")

teacher = Teacher("Семён", 25, "программирование")
print(teacher)
print(teacher.say_hello())
print(teacher.my_departament())
print("-============================-")

admin = Administration("Анна",25, "заведующая")
print(admin)
print(admin.say_hello())
print(admin.my_post())

print("-============================-")
func(pers)
func(stud)
func(teacher)