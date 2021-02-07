print('Calculator')
print('')

a = float(input('1 num: '))
b = float(input('2 num: '))
do = input('+, -, *, /: ')

if do == ('+'):
    c = a + b

if do == ('-'):
    c = a - b

if do == ('*'):
    c = a * b

if do == ('/'):
    c = a / b

print('Result: ' + str(c))
