# Задание
# Строительная компания нуждается в программе,
# которая бы по хотелкам клиента прикидывала
# смету и итоговую стоимость проекта.
#
# Существуют следующие классы:
# 1. Подвал
# - Тип фундамента
# - Подводимые коммуникации
# - Площадь
# - Мощность входной электрики
# 2. Этаж
# - Площадь
# - Кол-во комнат
# - Кол-во санузлов
# - Мощность входной электрики
# 3. Крыша
# - Наличие и площадь чердака
# - Тип крыши
# - Спутникая тарелка
# - Мощность входной электрики
# 4. Доп. постройки на территории
# - Площадь
# - Виды построек
# - Мощность входной электрики
# 5. Доп. опции
# - Виды опций
# Необходимо создать класс, который бы позволял
# по желанию клиента сконфигурировать объект
# Дом, внутри которого будут находится поля-объекты приведенных выше классов

from home import Home
from roof import Roof
from floor import Floor
from additional_options import AdditionalOptions as AddOpt
from additional_buildings import AdditionalBuildings as AddBuild
from basement import Basement as Base

def estimate(*objs: Home):
    total_cost = 0
    text_estimate = ""

    for obj in objs:
        total_cost += obj.total_cost()
        text_estimate += f"{obj.__str__()}\n---------------------"

    return (f"-------СМЕТА ДОМА-------\n"
            f"{text_estimate}\n"
            f"Общая стоимость всего дома: {total_cost:,} рублей")


basement = Base(area=200, type_basement="свайный",input_power=2000, communications=["Вода", "Газ","Электричество"])
floor_1 = Floor(area=100, floor_number=1, count_rooms=3, count_bathrooms=1, input_power=10000)
floor_2 = Floor(area=100, floor_number=2, count_rooms=3, count_bathrooms=1, input_power=10000)
roof = Roof(area=50, type_roof="плоская",input_power=2000, satellite=True)
add_opt = AddOpt(["a","b","c","d"])
add_build = AddBuild(area=200, input_power=10000, buildings=["a","b","c"])

print(estimate(basement, floor_1, floor_2, roof, add_opt, add_build))
