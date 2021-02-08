name = input('Name: ')
print('1) Russian')
print('2) USA')
print('3) Ukraine')
print('4) English')
print('5) Canada')
natsel = input('Select nation: ')
if natsel == ('1'):
    nat = ('Russian')
    town = ('Moscow')
if natsel == ('2'):
    nat = ('USA')
    town = ('California')
if natsel == ('3'):
    nat = ('Ukraine')
    town = ('Kiev')
if natsel == ('4'):
    nat = ('English')
    town = ('British')
if natsel == ('5'):
    nat = ('Canada')
    town = ('Ottava')
print('Civ')
print('')
print('')
print('Name: ' + str(name))
print('Nation: ' + nat)
print('Town: ' + town)
money = ('1000000000')
print('Money: ' + str(money) + '$')
nashap = 100
print('Citizen happy: ' + str(nashap) + '%')
ext = input('')
