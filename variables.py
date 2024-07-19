import random as r
import time


class Player():
    def __init__(self, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        self.hp = hp
        self.mana = mana
        self.resistance = resistance
        self.mag_resistance = mag_resistance
        self.mag_damage = mag_damage
        self.damage = damage
        self.attack_speed = attack_speed
        self.gold = 0
        super().__init__()


class Object():
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        self.rarity = rarity
        self.name = name
        self.add_hp = hp
        self.add_damage = damage
        self.add_resistance = resistance
        self.add_mag_damage = mag_damage
        self.add_mag_resistance = mag_resistance
        self.add_mana = mana
        self.add_attack_speed = attack_speed
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

        return rarity


class Sword(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        pass


class Axe(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        pass
            

class Bow(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        pass    


class Wand(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        pass


class Helmet(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        pass


class Chestplate(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        pass


class Leggings(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        pass


class Boots(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        pass


class Gold():
    def __init__(self) -> None:
        super().__init__()


def random_rarity(obj):
    rarity = None
    
    return rarity


player = Player(100, 10, 0, 0, 0, 10, 1.5)
print(str(Player))
BasicSword = Sword("BasicSword", "Common", 0, 0, 0, 0, 0, 10, 0)
print(str(BasicSword))
BrutalAxe = Axe("BrutalAxe", "Uncommon", 0, 0, 0, 0, 0, 15, 0.5)
print(str(BrutalAxe.name))
