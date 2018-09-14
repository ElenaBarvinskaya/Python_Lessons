# Задание С
# Реализуйте алгоритм поиска простых чисел "Решето Эратосфена" до заданного числа n
y = []
def resh(n):
    x = list(range(2, n+1))
    for i in range(2, n+1):
        for j in range(2, n+1):
            while i * j < n+1:
                a = i * j
                if a in y:
                    break
                else:
                    y.append(a)
            for a in x:
                if a in y:
                    x.remove(a)
    return print(x)
