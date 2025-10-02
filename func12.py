# Рекурсия (Ф-ция вызывает сома себя)
# Фибоначи: 0 1 1 2 3 5 8 12 21 34

import turtle as t  # as - это присваиваем ему псевдоним t
from operator import length_hint


# def factorial(n):  # Процедурный способ
#     result = 1  #
#     for i in range(2, n + 1):
#         result *= i
#     return result
#
#
# print(factorial(5))
#
# print()
#
#
# def factorial_r(n):
#     if n == 0:  # Базовое условие - выход из рекурсии (если нет, то stack overflow)
#         return 1
#     else:
#         return n * factorial_r(n - 1)
#
#
# print(factorial_r(4))


def tree(lenght):
    if lenght < 10:
        return
    t.forward(lenght)
    t.left(30)
    tree(lenght * 0.9)  # рекурсивный вызов
    t.right(60)
    tree(lenght * 0.9)  # рекурсивный вызов
    t.left(30)
    t.backward(lenght)
    t.left(90)

t.speed(0)
tree(100)
t.mainloop()
# Рисует черепашка