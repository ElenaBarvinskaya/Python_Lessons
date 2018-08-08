p=3.14
r=float(input("Введите радиус: "))
if r>0:
    L=2*p*r
    print('L=', L)
else:
    print('Ошибка')

#Второй вариант
def radius(r, p=3.14):
    return 2*p*r
