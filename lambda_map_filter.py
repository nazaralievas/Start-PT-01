# Лямбда-функция — это короткая, анонимная функция, которую мы пишем в одну строку.
# Она работает как обычная функция def, но без имени.
# lambda аргументы: выражение

# обычная функция:
def square(x):
    return x * x

# то же самое в виде лямбда-функции:
lambda x: x * x

# часто используется с функциями map, filter, sorted

# map() — применяет функцию ко всем элементам
# map(функция, список)
numbers = [1, 2, 3]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9]


# filter() — отфильтровает элементы по условию
# Оставляет только те элементы, для которых функция возвращает True
# filter(функция, список)
numbers = [1, 2, 3, 4, 5]
chetnye = list(filter(lambda x: x % 2 == 0, numbers))
print(chetnye)  # [2, 4]


# sorted() — сортирует список
# sorted(список, key=функция)
# key — это функция, по которой будет происходить сортировка (часто — lambda)
# sorted() не меняет исходный список, а возвращает новый отсортированный
# пример: сортировка строк по длине
words = ['apple', 'kiwi', 'banana']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['kiwi', 'apple', 'banana']
