# Сортировка по ключу с лямбда функцией

meals = ['бургер', 'пицца', 'шашлык', 'овощи', 'фрукты', 'конфеты', 'гречка']

participants = [
    ('Алиса', 27, 18),
    ('Борис', 19, 39),
    ('Владимир', 38, 63),
    ('Александр', 41, 95),
    ('Зинаида', 32, 61)
]

# Классическая лексиграфическая сортировка
# meals.sort()
# Сортировка по убыванию
meals.sort(reverse=True)  # именнованный... #Обратная сортировка

# По количеству букв
meals.sort(key=lambda x: len(x))

# По последней букве каждого слова
meals.sort(key=lambda x: x[-1])  #

#############################################
# Сортировка сложного списка #
# В лексикографическом порядке по имена
participants.sort()
print(participants)

# Сортировка по оценкам по убыванию
participants.sort(reverse= True, key=lambda x: x[-1])
print(participants)

# Сортировка по возрасту, а потом уже по оценкам и по возрастанию
participants.sort(key=lambda x: (x[1], x[2]), reverse=False)
print(participants)


print(meals)

# Sorted - принимает iterable object, возвращает отсортированный список
#reverse и key используются аналогично
# Пример: новый список, отсортированный по убыванию
sorted_meals = sorted(meals, reverse=True)
print(sorted_meals)