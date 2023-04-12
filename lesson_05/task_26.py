# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А
# в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8




def degree_calculator(number, degree):
    if degree == 1:
        return number
    else:
        return number * degree_calculator(number, degree - 1)

number = int(input("Введите число: "))
degree = int(input("Введите степень числа: "))
print(f"{number}**{degree} = {degree_calculator(number, degree)}")