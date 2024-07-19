import random as r
import time


class Player():
    def __init__(self) -> None:
        self.hp = 100
        self.mana = 10
        self.resistance = 0
        self.mag_resistance = 0
        self.mag_damage = 0
        self.damage = 10
        self.attack_speed = 1
        self.gold = 0
        self.lvl = 0
        super().__init__()


class Object():
    def __init__(self) -> None:
        self.rarity = ""
        self.name = ""
        self.add_hp = 0
        self.add_damage = 0
        self.add_resistance = 0
        self.add_mag_damage = 0
        self.add_mag_resistance = 0
        self.add_mana = 0
        self.add_attack_speed = 0
        self.lvl = 0
        super().__init__()

    def random_rarity(self):
        rarity = None
        random = r.randint(0, 100)

        if random >= 0 and random <= 50:
            rarity = "Common"
        elif random > 50 and random <= 80:
            rarity = "Uncommon"
        elif random > 80 and random <= 90:
            rarity = "Rare"
        elif random > 90 and random <= 97:
            rarity = "Mithic"
        else:
            rarity = "Legendary"


class Sword(Object):
    def __init__(self) -> None:
        super().__init__()


class Axe(Object):
    def __init__(self) -> None:
        super().__init__()
    

class Bow(Object):
    def __init__(self) -> None:
        super().__init__()    


class Wand(Object):
    def __init__(self) -> None:
        super().__init__()


class Helmet(Object):
    def __init__(self) -> None:
        super().__init__()


class Chestplate(Object):
    def __init__(self) -> None:
        super().__init__()


class Leggings(Object):
    def __init__(self) -> None:
        super().__init__()


class Boots(Object):
    def __init__(self) -> None:
        super().__init__()


class Gold():
    def __init__(self) -> None:
        super().__init__()


def random_rarity(obj):
    rarity = None
    
    return rarity


BasicSword = Sword()
BasicSword.name = "Basic Sword"
BasicSword.rarity = "Common"
