# Часть 1
print("Пожалуйста, введите ваше имя")
firtName = input()
print("Пожалуйста, введите вашу фамилию")
secondName = input()
print("Добрый день, {0} {1}, рады приветствовать вас!".format(firtName, secondName))
pass

# Часть 2
print("Введите первое число:")
firstName = float(input())
if type(firstName)==str:
    pass
else:
    print('{:.1%}'.format(firstName))
print("Введите второе число:")
secondName = float(input())
if type(firstName)==str:
    pass
else:
    print('{:,.2f}$'.format(secondName))
