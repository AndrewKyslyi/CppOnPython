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
        self.lvl = 0
        super().__init__()


class Object():
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean) -> None:
        self.rarity = rarity
        self.name = name
        self.add_hp = hp
        self.add_damage = damage
        self.add_resistance = resistance
        self.add_mag_damage = mag_damage
        self.add_mag_resistance = mag_resistance
        self.add_mana = mana
        self.add_attack_speed = attack_speed
        self.lvl = 0
        self.status = boolean
        super().__init__()

    def add_to_inventory(self):
        Inventory1.space -= 1


class Sword(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean) -> None:
        super().__init__(rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean)



class Axe(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean) -> None:
        super().__init__(rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean)
            

class Bow(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean) -> None:
        super().__init__(rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean)


class Wand(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean) -> None:
        super().__init__(rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean)


class Helmet(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean) -> None:
        super().__init__(rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean)


class Chestplate(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean) -> None:
        super().__init__(rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean)



class Leggings(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean) -> None:
        super().__init__(rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean)



class Boots(Object):
    def __init__(self, rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean) -> None:
        super().__init__(rarity, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl, boolean)


class Gold():
    def __init__(self) -> None:
        self.amount = 0
        super().__init__()


class Inventory():
    def __init__(self) -> None:
        self.space = 50
        super().__init__()


player = Player(100, 10, 0, 0, 0, 10, 1.5)

BasicSword = Sword("Common", "Basic Sword", 0, 0, 0, 0, 0, 10, 0, 0, False)
print(BasicSword)
BrutalAxe = Axe("Uncommon", "Brutal Axe", 0, 0, 0, 0, 0, 15, 0.5, 0, False)
print(BrutalAxe)
BasicBow = Bow('Common', "Basic Bow", 0, 0, 0, 0, 0, 10, 0.5, 0, False)
print(BasicBow)
MagicStaff = Wand('Rare', 'Magic Staff', 0, 50, 0, 1, 35, 0, -0.2, 0, False)

AnubisHelmet = Helmet("Mythic", "Anubis Helmet", 50, 80, 10, 5, 0, 0, -0.2, 0, False)

KnightChestplate = Chestplate("Rare", "Knight's Chestplate", 100, 10, 15, 0, 0, 0, 0.3, 0, False)

LEATHERPANTS = Leggings('Legendary', 'LEATHER PANTS', 100, 15, 30, 10, 10, 1, -0.7, 0, False)

BarhatnyeTyagi = Boots('Uncommon', "Barhatnye Tyagi", 10, 1, 5, 7, 0, 0, -0.2, 0, False)
print(BarhatnyeTyagi)
all_objects = (BasicSword, BrutalAxe, BasicBow, MagicStaff, AnubisHelmet, KnightChestplate, LEATHERPANTS, BarhatnyeTyagi)

all_rarities = ('Common', 'Uncommon', 'Rare', 'Mythic', 'Legendary')

Inventory1 = Inventory()
