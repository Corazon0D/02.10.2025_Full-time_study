# Декораторы
import time
# 1. Функцию можно переопределить
language = 'en'

if language == 'en':
    def greet(name):
        print('Hello,', name)
else:
    def greet(name):
        print('Привет,', name)

greet('Дмитрий')


# Лучше пользоваться Декоратором
# Это ф-ция принимающая другую ф-цию
# В качестве аргумента и меняет ёё поведение

# Определяем простой Декоратор

def my_decorator(func):
    def wrapper():  # обёртка без параметров
        print('Действия до вызова переданной Ф-ции')
        func()  # Вызов переданной функции
        print('Действия после вызова переданной Ф-ции')

    return wrapper


@my_decorator
def called_func():
    print('Вызываемая Ф-ция')


called_func()


# Декоратор с параметрами

def params_decorator(func):
    def wrapper(*args, **kwargs):
        print('Задекорированная Ф-ция вызвана с параметрами: ', args, kwargs)
        result = func(*args, **kwargs)
        print('Результат этой Ф-ции', result)
        return result

    return wrapper


@params_decorator
def summ(a, b, action='s'):
    if action =='s':
        return a + b
    return a * b


res = summ(3, 4, action='m')
print(res)


# Измерение времени работы Ф-ции

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # время старта
        result = func(*args, **kwargs)
        end_time = time.time() # Время окончания
        print(f'Ф-ция {func.__name__} выполнялось {end_time - start_time:.2f} сек.')
        return result
    return wrapper

@timing_decorator
def some_function():
    a =[]
    print('Начало работы')
   # time.sleep(2) # Задержка в 2 сек.
    for i in range (1000000):
        a.append(i)
    print('окончание работы')

some_function()