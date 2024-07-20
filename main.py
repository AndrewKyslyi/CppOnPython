import random as r
import time
import variables as v
from threading import Thread

#thread1 = Thread(target=hello())
#thread2 = Thread(target=world())

def random_rarity():
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

def get_color(rarity):
    colors = {
        "Common": "\033[90m",  # Серый
        "Uncommon": "\033[96m",  # Светло-голубой
        "Rare": "\033[94m",  # Синий
        "Mythic": "\033[91m",  # Красный
        "Legendary": "\033[93m"  # Желтый
    }
    return colors.get(rarity)

def reset_color():
    return "\033[0m"


def update_stats(player, inventory):
    for i in inventory:
        if i.status:
            for j in i:
                if j is int:
                    for i in player:

            


while True:
    print('Hello! This is "World Of Magic"\nIn this universe u can choose any way u like! Maybe its just like "open-world" console game xD\nHope ull have fun!')
    time.sleep(3)
    print("So...")
    time.sleep(1)
    print("Lets start!")
    random_rarity_list = []

    while len(random_rarity_list) < 3:
        for i in v.all_objects:
            if random_rarity() == i.rarity:
                if i in random_rarity_list:
                    continue
                else:
                    random_rarity_list.append(i)
                print(i.rarity)
                break

    # using enumerate() to count ids
    for index, i in enumerate(random_rarity_list, start=1):
        color = get_color(i.rarity)
        reset = reset_color()
        print(f'{index}. {i.name} - {color}{i.rarity}{reset}')
    
    
    while True:
        try:
            answer = int(input("Choose number (1, 2 or 3): "))    
        except ValueError:
            print("U may printed wrong data")
            continue

        if answer != 1 and answer != 2 and answer != 3:
            continue
        else: 
            break

    if answer == 1:
        v.Inventory1.space -= 1
        v.Inventory1.obtained.append(random_rarity_list[0])
    elif answer == 2:
        v.Inventory1.space -= 1
        v.Inventory1.obtained.append(random_rarity_list[1])
    if answer == 3:
        v.Inventory1.space -= 1
        v.Inventory1.obtained.append(random_rarity_list[2])
    
    print(f"U obtained new item {random_rarity_list[answer-1].rarity}")
    answer = str(input("Do u wanna equip it(y/n)?\nAnswer: "))

    if answer == 'y':
        v.Inventory1.obtained[-1].status = True
        
    random_rarity_list = []
    break


