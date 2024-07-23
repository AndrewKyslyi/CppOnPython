import random as r
import time


class Player():
    def __init__(self, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed) -> None:
        """self.hp = hp
        self.mana = mana
        self.resistance = resistance
        self.mag_resistance = mag_resistance
        self.mag_damage = mag_damage
        self.damage = damage
        self.attack_speed = attack_speed"""
        self.gold = 0
        self.lvl = 0
        self.stats = {
                "hp": hp,
                "mana": mana,
                "resistance": resistance,
                "mag_resistance": mag_resistance,
                "mag_damage": mag_damage,
                "damage": damage,
                "attack_speed": attack_speed,

                }
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


class Goblin(Object):
    def __init__(self, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl) -> None:
        super().__init__(name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl)


class EliteGoblin(Object):
    def __init__(self, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl) -> None:
        super().__init__(name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl)


class GrandOrc(Object): 
    def __init__(self, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl) -> None:
        super().__init__(name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl)


class TheBoss(Object):
     def __init__(self, name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl) -> None:
        super().__init__(name, hp, mana, resistance, mag_resistance, mag_damage, damage, attack_speed, lvl)



class Gold():
    def __init__(self) -> None:
        self.amount = 0
        super().__init__()


class Inventory():
    def __init__(self) -> None:
        self.space = 50
        self.obtained = []  
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

Goblin1 = Goblin('Goblin', 100, 20, 0, 0, 0, 10, 2, 1)
Elite_goblin = EliteGoblin('Elite Goblin', 250, 50, 10, 10, 20, 30, 1.5, 1)
Grand_Orc = GrandOrc('Grand Orc', 500, 100, 15, 10, 20, 50, 2.5, 1)
The_Boss = TheBoss("TheBoss", 1000, 125, 30, 30, 50, 80, 2, 1)
