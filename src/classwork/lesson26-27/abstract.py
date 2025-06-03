# Абстрактные классы

# Необходимо реализовать систему классов для оружия в игре
# Пистолеты, автоматы, снайперская винтовка и БФГ

# Gun (оружие) - стрелять, целится, перезарежаться и урон(п)
# Pistol
# AutoGun
# Snipe
# BFG

import abc # Библиотека для создания абстрактных классов

class Gun(abc.ABC):
    _damage = 0
    _bullets = 0

    def __init__(self, damage: int = 0, bullet_count : int = 0):
        self._damage = damage
        self._bullets = bullet_count

    def __del__(self):
        pass

    @abc.abstractmethod
    def fire(self):
        pass

    @abc.abstractmethod
    def aim(self):
        pass

    @abc.abstractmethod
    def reload(self):
        pass

    def __str__(self):
        return f"This is class GUN"

class BFG(Gun):

    def __init__(self, damage: int = 0, bullet_count: int = 0):
        super().__init__(damage, bullet_count)

    def __del__(self):
        pass

    def fire(self):
        pass

    def aim(self):
        pass

    def reload(self):
        pass

    def __str__(self):
        return f"This is class BFG"

bfg = BFG(10)
print(bfg)