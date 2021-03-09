import random
from random import randint
import os
import webbrowser
name = input('Name:  ')
hp_list = [('100'), ('75'), ('50')]
hp = random.choice(hp_list)
print('HP: ' + str(hp))
lvl = randint(1, 50)
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
petlvl = randint(1, 10)
print('LVL: ' + str(petlvl))
print('')
items = 'No'
print('Items: ' + str(items))
print('')
warrior_list = ['Cobra', 'Snake', 'Eagle']
warrior = random.choice(warrior_list)
print('Warrior: ' + str(warrior))
warriorhp = randint(0, 100)
print('HP: ' + str(warriorhp))
warriorlvl = randint(1, 10)
print('LVL: ' + str(warriorlvl))
ext = input('')
