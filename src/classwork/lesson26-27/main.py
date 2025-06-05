from automobile import Automobile
from sedan import Sedan
from suv import SUV
from cargo import Cargo
from interface import Interface

def info_auto(obj: Automobile):
    return obj.get_info()

def drive(obj: Interface):
    print()
    print(obj.start_engine())
    print(obj.forward_moving())
    print(obj.backward_moving())
    print(obj.hand_brake())

sedan_1 = Sedan(name="Лада", power_engine=120, price=1_200_000)
suv_1 = SUV(name="Уаз", power_engine=240, price=2_400_000)
cargo_1 = Cargo(name="Белаз", power_engine=360, price=3_600_000, tonnage=240)

# auto = Automobile()
sedan_1.transmission_box = "АКПП"
sedan_1.additional_option = 5
print(info_auto(sedan_1))
drive(sedan_1)
print()

print(info_auto(suv_1))
drive(suv_1)
print()

print(info_auto(cargo_1))
drive(cargo_1)

# print()
# print(info_auto(auto))