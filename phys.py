print('Physic Helper')
print('')
print('1) Скорость, время, расстояние')
print('2) Плотность, масса, объем')
print('3) Силы')
print('4) Давление')
formsel = input('Выберите формулу: ')

if formsel == ('1'):
	print('Скорость время, расстояние')
	print('')
	print('1) Скорость')
	print('2) Время')
	print('3) Расстояние')
	scorvrras = input('Выберите формулу: ')
	if scorvrras == ('1'):
		print('Скорость')
		print('')
		print('v = s / t')
		s = float(input('Введите путь (s) : '))
		t = float(input('Введите время (t) : '))
		v = s / t
		print('v = ' + str(v))
	if socrvrras == ('2'):
		print('Время')
		print('')
		print('t = s / v')
		s = float(input('Введите путь (s) : '))
		v = float(input('Введите скорость (v) : '))
		t = s / v
		print('t = ' + str(t))
	if scorvrras == ('3'):
		print('Расстояние')
		print('')
		print('s = v * t')
		v = float(input('Введите скорость (v) : '))
		t = float(input('Введите время (t) : '))
		s = v * t
		print('s = ' + str(s))
if formsel == ('2'):
	print('Плотность, масса, объем')
	print('')
	print('1) Плотность')
	print('2) Масса')
	print('3) Объем')
	plotmasob = input('Выберите формулу: ')
	if plotmasob == ('1'):
		print('Плотность')
		print('')
		print('P = m / V')
		m = float(input('Введите массу (m) : '))
		V = float(input('Введите объем (V) : '))
		P = m / V
		print('P = ' + str(P))
	if plotmasob == ('2'):
		print('Масса')
		print('')
		print('m = P * V')
		P = float(input('Введите плотность (p) : '))
		V = float(input('Введите объем (V) : '))
		m = P * V
		print('m = ' + str(m))
	if plotmasob == ('3'):
		print('Объем')
		print('')
		print('V = m / P')
		m = float(input('Введите массу (m) : '))
		P = float(input('Введите плотность (P) : '))
		V = m / P
		print('V = ' + str(V))
if formsel == ('3'):
	print('Силы')
	print('')
	print('1) Сила тяжести')
	print('2) Сила упругости')
	print('3) Вес')
	silasel = input('Выберите формулу: ')
	if silasel == ('1'):
		print('Сила тяжести')
		print('')
		print('Fт = m * g')
		g = 10
		print(g)
		m = float(input('Введите массу: '))
		ft = m * g
		print('Fт = ' + str(ft))
	if silasel == ('3'):
		print('Вес')
		print('')
		print('P = Fт = m * g')
		g = 10
		print(g)
		m = float(input('Введите массу: '))
		ft = m * g
		print('P = ' + str(ft))
if formsel == ('4'):
	print('Давление')
	print('')
	print('1) Земное')
	print('2) В жидкости и газе')
	davsel = input('Выберите формулу: ')
	if davsel == ('1'):
                print('Земное давление')
                print('')
                print('1) 1 метод')
                print('2) 2 метод')
                davmetsel = input('Выберите метод: ')
                if davmetsel == ('1'):
                        print('1 метод')
                        print('')
                        print('P = Fт / S')
                        ft = float(input('Введите силу тяжести (Fт): '))
                        s = float(input('Введите площадь (S): '))
                        P = ft / s
                        print('P = ' + str(P))
                if davmetsel == ('2'):
                        print('2 метод')
                        print('')
                        g = 10
                        print('p = m * g / s')
                        m = float(input('Введите массу (m): '))
                        a = m * g
                        s = float(input('Введите площадь (S): '))
                        print('g = ' + str(g))
                        b = a / s
                        print('p = ' + str(b))
        if davsel == ('2'):
                print('Давление в жидкости и газе')
                print('')
                print('p = p * h * g')
                g = 10
                ps = float(input('Введите давление (p): '))
                h = float(input('Введите высоту (h): '))
                print('g = ' + str(g))
                pv = ps * h * g
                print('p = ' + str(pv))
ext = input('')
