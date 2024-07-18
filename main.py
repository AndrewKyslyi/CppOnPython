import _random as _r


class Player():
    def __init__(self) -> None:
        self.hp = 100
        self.mana = 10
        self.resistance = 0
        self.mag_resistance = 0
        self.mag_damage = 0
        self.damage = 10
        super().__init__()


class Weapon():
    def __init__(self) -> None:
        self.rarity = ""
        self.name = ""
        self.add_hp = 0
        self.add_damage = 0
        self.add_resistance = 0
        self.add_mag_damage = 0
        self.add_mag_resistance = 0
        self.add_mana = 0
        super().__init__()

    
class Sword(Weapon):
    def __init__(self) -> None:
        super().__init__()
        

BasicSword = Sword()
BasicSword.name = "Basic Sword"
BasicSword.rarity = "Common"
print(BasicSword.name)
