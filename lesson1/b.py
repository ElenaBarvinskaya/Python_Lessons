import math
s = float(input("Введите площадь круга: "))
if s > 0:
    x = s * math.pi
    y = math.sqrt(x)
    L = 2 * y
    print('L =', L)
else:
    print('Ошибка')

#Второй вариант
def area(s):
    return 2*math.sqrt(s*math.pi)
