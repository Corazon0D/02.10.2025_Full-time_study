# Встроенные модули
# Не импортируем то чем не пользуемся
# import math as m # приводим через as
# import math as m
#
# print(dir(m))
# from math import pi, e, sqrt
#
# print(f'Число Пи:', m.pi)
# print(f'Применим ceil r Pi:', m.ceil(m.pi))
# print(f'Основание натурального логарифма:', e)
# print(f'Квадратный корень из 225:', sqrt(225))

# ord и chr для работы только с символами
# Узнаём код по символу
letter = 'r'
code = ord(letter)
print(code)

# Узнаём символ по коду
# « - 171
# » - 187
# ⚀ - 9856
# ⚁ - 9857
# ⚂ - 9858
# ⚃ - 9859
# ⚄ - 9860
# ⚅ - 9861
symbol = chr(9861)
print(symbol)

print(f'Кафе {chr(171)}Аист{chr(187)}')