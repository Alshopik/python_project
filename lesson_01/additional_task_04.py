#Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

#РЕШЕНИЕ:
# s = p + k + c
# p = c
# k = 2*(p + c) = 2*(p + p) = 4*p
# s = p + 4*p + p = 6*p
# p = s/6
# c = s/6
# k = 4*p

s = int(input('Введите количество журавликов: '))
p = s // 6
c = p
k = 4 * p
print(p, k, c)