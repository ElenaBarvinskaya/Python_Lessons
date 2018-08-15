# Часть 1
words = ['мудак', 'козел', 'дебил', 'урод', 'курица', 'тварь', 'дура']
print('Введите фразу в формате: Ну ты <какое-то слово>!')
str = input()
strNew = str[:-1]
if ( strNew[6:] in words ):
    print('Поправочка: Ну ты *****!')
else:
    pass

# Часть 1. Вариант 2.
words = ['мудак', 'козел', 'дебил', 'урод', 'курица', 'тварь', 'дура', 'дурак']
x = ['****']
str = input('Пожалуйста, введите фразу: ')
s2 = str.split()
for word in s2:
    for mat in words:
        if mat == word:
            s2[s2.index(word)] = x[0]
        else:
            pass
str = " ".join(s2)
print(str)

# Часть 2
words = ['редиска', 'дурак', 'мудак']
words = {"редиска" :'нехороший человек',
         "дурак" : 'человек с альтернативным мнением',
         "мудак" : 'человек с сомнительными моральными принципами'}
s = input('Пожалуйста, введите фразу: ')
s2 = s.split()
for word in s2:
    for mat in words:
        if mat == word:
            s2[s2.index(word)] = words[word]
        else:
            pass
s = " ".join(s2)
print(s)