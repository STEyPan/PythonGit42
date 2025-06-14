from money import Money
from usd import USD
from rub import Rub
from euro import Euro

def sum_money(obj_1: Money, obj_2: Money):
    return f"Сумма: {obj_1 + obj_2}"

def update_info(obj: Money,
                whole : int,
                cent : int):
    obj.whole = whole
    obj.cent = cent

    return obj


usd_1 = USD(199,99)
usd_2 = USD(199,1)
update_info(usd_1, 100, 99)
update_info(usd_2, 199, 99)
print(sum_money(usd_1, usd_2))
print("-=================================================-")

rub_1 = Rub(199,99)
rub_2 = Rub(199,99)
print(sum_money(rub_1, rub_2))
print("-=================================================-")

euro_1 = Euro(199,99)
euro_2 = Euro(199,99)
print(sum_money(euro_1, euro_2))
print("-=================================================-")