# Часть 1
print("Пожалуйста, введите ваше имя")
firstName = input()
print("Пожалуйста, введите вашу фамилию")
secondName = input()
print("Пожалуйста, введите ваш возраст")
age = int(input())
print("Пожалуйста, введите ваш адрес")
adress = input()
print("Пожалуйста, введите ваш телефон!")
phone = input()
print("Ваши данные")
print("""\
Имя: {0}
Фамилия: {1}
Возраст: {2}
Адрес: {3}
Телефон: {4}""".format(firstName, secondName, age, adress, phone))
pass

# Часть 2
print("Пожалуйста, введите ваше имя")
firstName = input()
print("Пожалуйста, введите вашу фамилию")
secondName = input()
print("Пожалуйста, введите ваш возраст")
age = int(input())
print("Пожалуйста, введите ваш пол")
sex = input()
if (age < 10 and sex == 'Мужской'):
    print('Привет, малыш {0}, в холодильнике есть мороженое для тебя'.format(firstName))
elif (age > 10 and age < 18 and sex == 'Мужской'):
    print('Здравствуй, {0}. Совсем взрослый стал! Пошли посмотрим новых Фантастических тварей'.format(firstName))
elif (age > 18 and age < 40 and sex == 'Мужской'):
    print('Привет, {0}. Смотрел вчера игру?'.format(firstName))
elif (age > 40 and sex == 'Мужской'):
    print('Добрый день, господин {0}, на почте свежие котировки акций'.format(secondName))
elif (age < 10 and sex == 'Женский'):
    print('Привет, {0}-Зайка, в холодильнике есть мороженое для тебя'.format(firstName))
elif (age > 10 and age < 18 and sex == 'Женский'):
    print('Привет, {0}. Совсем красавица стала! Я тут присмотрела новую юбочку для тебя'.format(firstName))
elif (age > 18 and age < 40 and sex == 'Женский'):
    print('Здравствуйте, {0}. Напишите, пожалуйста, когда вам будет удобно встретиться'.format(firstName))
elif (age > 40 and sex == 'Женский'):
    print('Добрый день, госпожа {0}, на почте расписание ваших встреч на сегодня'.format(secondName))
else:
    pass
