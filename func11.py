# Потоковый ввод stdin
# Поток, который поддерживает Python: stdin (вход), stdout (выход), stderr (ошибка)
# Прекращение потока: Ctrl + D (Pycharm и Linux)
# прекращение потока: Ctrl + Z и Enter (консоль Windows)
import sys


data =  sys.stdin.readlines()

data = list(map(lambda x: x.rstrip('\n'), data))

print(data)

# Стандартный набор ввода
# for s in sys.stdin:
#     print(s)

# sys.stdout.write('Привет\n')
# sys.stdout.write('Пока\n')
# sys.stderr.write('Ошибка\n')
#
# print('Сообщение', file=sys.stderr)

