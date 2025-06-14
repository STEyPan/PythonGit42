from ship import Ship
from frigate import Frigate
from destroyer import Destroyer
from cruiser import Cruiser

def ship_info(obj: Ship):
    return obj.get_info()

def ship_moving(obj: Ship):
    return (f"{obj.start_engine()}\n"
            f"{obj.move_forward()}\n"
            f"{obj.move_right()}\n"
            f"{obj.move_left()}\n"
            f"{obj.move_back()}\n"
            f"{obj.stop_engine()}")


frigate_1 = Frigate(name="Адмирал Горшков", country="Россия",
                    displacement=4000, speed=30,
                    armament=["ПВО","Артиллерия", "Торпеды"],
                    sonar_type="ГАС 'Заря-МЭ'")
print(ship_info(frigate_1))
print()
print(ship_moving(frigate_1))
print("-=================================-")