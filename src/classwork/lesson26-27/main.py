from automobile import Automobile
from sedan import Sedan
from suv import SUV
from cargo import Cargo


def get_info_auto(obj: Automobile):
    return obj.get_info()

sedan_1 = Sedan()
suv_1 = SUV()
cargo_1 = Cargo()

# auto = Automobile()

sedan_1.additional_option = 5
print(get_info_auto(sedan_1))
print()
print(get_info_auto(suv_1))
print()
print(get_info_auto(cargo_1))
# print(main(auto))
