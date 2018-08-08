import math
a=float(input("Введите число a: "))
if type(a)==str:
    print('Ошибка. Введите число')
else:
    print('a =', a)
b=float(input("Введите число b: "))
if type(b)==str:
    print('Ошибка. Введите число')
else:
    print('b =', b)
c=float(input("Введите число c: "))
if type(c)==str:
    print('Ошибка. Введите число')
else:
    print('c =', c)
if (type(a)==str or type(b)==str or type(c)==str):
    pass
else:
    result = b ** 2 - 4 * a * c
    if result < 0 :
        print("Корень из отрицательного числа не извлекается")
    else:
        x = (-b + math.sqrt(result)) / 2 * a
        y = (-b - math.sqrt(result)) / 2 * a
        print(x, y)
