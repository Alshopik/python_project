# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()

def my_func1(a, b, c):
    d = [a, b, c]
    print(d)
    d.sort()
    print(d)
    return d[1] + d[2]

def my_func2(a, b, c):
    d = [a, b, c]
    print(d)
    d.remove(min(a, b, c))
    print(d)
    return sum(d)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print(my_func1(a, b, c))

print(my_func2(a, b, c))