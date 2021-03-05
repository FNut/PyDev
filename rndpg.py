import random
from random import randint
import os
import webbrowser
name = input('Name:  ')
hp_list = [('100'), ('75'), ('50')]
hp = random.choice(hp_list)
print('HP: ' + str(hp))
lvl = randint(0, 50)
print('LVL: ' + str(lvl))
gold = randint(0, 1000)
print('Gold: ' + str(gold))
print('')
pet_list = ['Dog', 'Cat']
pet = random.choice(pet_list)
print('Pet: ' + str(pet))
petname = input('Name: ')
pethp_list = ['10', '25', '50']
pethp = random.choice(pethp_list)
print('HP: ' + str(pethp))
petlvl = randint(0, 10)
print('LVL: ' + str(petlvl))
print('')
ext = input('')
