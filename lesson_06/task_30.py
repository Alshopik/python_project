# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

element_1 = int(input("Введите первый элемент прогрессии: "))
difference = int(input("Введите разность элементов прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

# arr = list()
# for i in range(n):
#     arr.append(element_1 + i * difference)
# print(arr)

for i in range(n):
    print(element_1 + i * difference)