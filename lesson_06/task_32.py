# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

rand_list = []
n = 10
for i in range(n):
    rand_list.append(random.randint(-10, 10))
print(rand_list)

min_num = int(input("Введите нижнюю границу диапазона: "))
max_num = int(input("Введите верхнюю границу диапазона: "))
for i in range(len(rand_list)):
    if min_num <= rand_list[i] <= max_num:
        print(i, end=' ')

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)