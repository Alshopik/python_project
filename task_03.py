"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input('Введите число n: '))
print(f'n + nn + nnn = {n}{n*2}{n*3}')