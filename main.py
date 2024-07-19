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


while True:
    print('Hello! This is "World Of Magic"\nIn this universe u can choose any way u like! Maybe its just like "open-world" console game xD\nHope ull have fun!')
    time.sleep(3)
    print("So...")
    time.sleep(1)
    print("Lets start!")
    for_random = []
    for _ in range(0,3):
        for i in v.all_objects:
            if random_rarity() == i.rarity:
                for_random.append(i.name)
                print(i.rarity)
                break
    

    print(for_random)
    print(f"Выбирай что по душе ;)\n\n{for_random[0]}\n\n{for_random[1]}\n\n{for_random[2]}\n")
    for_random = []
    break



