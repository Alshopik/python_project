# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def sum_calculator(number1, number2):
    if number2 == 0:
        return number1
    else:
        return sum_calculator(number1, number2 - 1) + 1

number1 = int(input("Введите натуральное число: "))
number2 = int(input("Введите еще одно натуральное число: "))
print(f"{number1}+{number2}={sum_calculator(number1, number2)}")