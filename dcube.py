import random
d6_list = [1, 2, 3, 4, 5, 6]
d12_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d20_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('1) D6')
print('2) D12')
print('3) D20')
cubesel = input('Select cube: ')
print('')
if cubesel == ('1'):
    print('Num: ', random.choice(d6_list)) 
if cubesel == ('2'):
    print('Num:', random.choice(d12_list))
if cubesel == ('3'):
    print('Num:', random.choice(d20_list))
ext = input('')