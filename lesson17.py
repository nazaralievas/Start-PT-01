# Разберём домашку:
# grades = [[3, 4, 3, 5], [3, 4, 3, 3]]
# Это список с оценками учеников двух классов.
# У всех учеников второго класса повысьте оценку на 1 балл.
# У вас должен получиться такой список:
# [[3, 4, 3, 5], [4, 5, 4, 4]]

grades = [[3, 4, 3, 5], [3, 4, 3, 3]]
grades[1] == [3, 4, 3, 3]
for i in range(len(grades[1])):
    grades[1][i] = grades[1][i] + 1

print(grades) # [[3, 4, 3, 5], [4, 5, 4, 4]]

# решение с помощью list comprehension
grades = [[3, 4, 3, 5], [3, 4, 3, 3]]
grades[1] = [grade + 1 for grade in grades[1]]
print(grades) # [[3, 4, 3, 5], [4, 5, 4, 4]]


# list comprehension позволяет создать список в одну строку
# если бы мы хотели создать список чётных чисел от 1 до 10 включительно
#не зная list comprehension мы бы написали:
lst = []
for num in range(1, 11):
    if num % 2 == 0:
        lst.append(num)

print(lst) # [2, 4, 6, 8, 10]

# с помощью list comprehension мы можем получить такой список просто написав всё внутри []
lst = [num for num in range(1, 11) if num % 2 == 0]
print(lst) # [2, 4, 6, 8, 10]


# с помощью list comprehension мы можем создать список на основе другого списка
# создайте список positive_nums где будут только положительные числа из списка nums 
nums = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
positive_nums = [num for num in nums if num > 0]
print(positive_nums) # [1.25, 10.22, 3.78, 1.16]

# простой вариант решения этой задачи выглядел бы так:
nums = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
positive_nums = []
for num in nums:
    if num > 0:
        positive_nums.append(num)

print(positive_nums) # [1.25, 10.22, 3.78, 1.16]


# else тоже можно использовать в list comprehension. Покажу на примере следующей задачи:
# создайте список new_lst, где будут положительные числа из списка nums
# а вместо отрицательных будут нули
nums = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_lst = [num if num > 0 else 0 for num in nums]
print(new_lst) # [1.25, 0, 10.22, 3.78, 0, 1.16]

# не сокращенный вариант решения этой задачи:
new_lst = []
for num in nums:
    if num > 0:
        new_lst.append(num)
    else:
        new_lst.append(0)


# задание: создайте список even_nums с чётными числами из списка nums
# а вместо нечётных чисел должна быть строка 'нечёт'
nums = [4, 3, 8, 9, 1, 5, 12, 6]
even_nums = [num if num % 2 == 0 else 'нечёт' for num in nums]
print(even_nums) # [4, 'нечёт', 8, 'нечёт', 'нечёт', 'нечёт', 12, 6]

# не сокращенный вариант решения этой задачи:
nums = [4, 3, 8, 9, 1, 5, 12, 6]
new_lst = []
for num in nums:
    if num % 2 == 0:
        new_lst.append(num)
    else:
        new_lst.append('нечёт')


# задание: создайте список lst с длинами строк из списка products.
# lst должен выглядеть вот так: [5, 6, 4, 3]
products = ['apple', 'banana', 'kiwi', 'pie']
lst = [len(p) for p in products]
print(lst) # [5, 6, 4, 3]

# не сокращенный вариант решения этой задачи:
products = ['apple', 'banana', 'kiwi', 'pie']
lst = []
for p in products:
    lst.append(len(p))

print(lst) # [5, 6, 4, 3]


# разберём функцию zip, которая позволяет "сшивать" два списка
# например, у нас есть две группы студентов: boys и girls
# нужно объединить студентов в команды по два человека: один из boys и одна из girls
boys = ['Shabdan', 'Dmitriy', 'Aidin']
girls = ['Anzhelika', 'Aiday', 'Aibiyke']
for b, g in zip(boys, girls):
    print(f"Проект делают: {b} и {g}")
# Проект делают: Shabdan и Anzhelika
# Проект делают: Dmitriy и Aiday
# Проект делают: Aidin и Aibiyke

# функцию zip можно использовать и в list comprehension
# создадим вложенный список с парами студентов:
boys = ['Shabdan', 'Dmitriy', 'Aidin']
girls = ['Anzhelika', 'Aiday', 'Aibiyke']
result = [[b, g] for b, g in (zip(boys, girls))]
print(result) # [['Shabdan', 'Anzhelika'], ['Dmitriy', 'Aiday'], ['Aidin', 'Aibiyke']]

# не сокращённый вариант решения задачи:
boys = ['Shabdan', 'Dmitriy', 'Aidin']
girls = ['Anzhelika', 'Aiday', 'Aibiyke']
result = []
for b, g in zip(boys, girls):
    result.append([b, g])
print(result) # [['Shabdan', 'Anzhelika'], ['Dmitriy', 'Aiday'], ['Aidin', 'Aibiyke']]


# задание: с помощью функции zip сложите элементы списков nums1 и nums2
# нулевой элемент с нулевым, первый с первым, второй со вторым
nums1 = [1, 3, 8, 3]
nums2 = [4, 3, 8, 9]
result = [n1 + n2 for n1, n2 in zip(nums1, nums2)]
print(result) # [5, 6, 16, 12]

# не сокращенный вариант решения этой задачи:
nums1 = [1, 3, 8, 3]
nums2 = [4, 3, 8, 9]
result = []
for n1, n2 in zip(nums1, nums2):
    result.append(n1 + n2)

print(result) # [5, 6, 16, 12]


# перейдём к следующей большой теме: СЛОВАРИ (на англ. - DICTIONARY)
# этот тип данных позволяет хранить данные еще удобнее
# элементы состоят из пары ключ-значение
# создадим словарь grades, в котором ключами будут названия предметов, а значениями оценка за этот предмет
grades = {'biology': 4,
          'math': 4,
          'geography': 5}

# чтобы вывести нужный элемент словаря нужно обратиться по ключ
# узнаем оценку за географию:
print(grades['geography']) # 5

# чтобы добавить новую пару ключ-значение в словарь, нужно написать ключ в квадратных скобках, знак =, и значение
grades['history'] = 5
print(grades) # {'biology': 4, 'math': 4, 'geography': 5, 'history': 5}

# чтобы изменить значение ключа, делаем то же самое. Давайте исправим оценку за биологию:
grades['biology'] = 5
print(grades) # {'biology': 5, 'math': 4, 'geography': 5, 'history': 5}


# удалить элемент словаря можно с помощью метода pop
# удалим данные о математике
grades.pop('math')
print(grades) # {'biology': 5, 'geography': 5, 'history': 5}

# так же удалить можно с помощью оператора del
# удалим данные о биологии
del grades['biology']
print(grades) # {'geography': 5, 'history': 5}


# pop позволяет не только удалить элемент, но и сохранить значение в переменной
d = grades.pop('history') # удаляем элемент под ключом 'history' и сохраняем его значение в переменной d
print(d) # [5]
print(grades) # {'geography': 5} теперь в словаре осталась только геометрия


# ключами в словарях могут быть только неизменяемые типы данных: строки, числа, кортежи и frozenset (последние два пройдём на следующих уроках)
# а значениями могут быть любые типы данных, например списки
student1 = {
    'name': 'Mike',
    'age': 16,
    'subjects': ['bio', 'math', 'history'],
    'contract': False
}

# чтобы вывести предметы студента, как обычно обращаемся по ключу:
print(student1['subjects']) # ['bio', 'math', 'history']

# чтобы вывести имя:
print(student1['name']) # Mike

# если мы обратимся к несуществующему ключу, например 'gender', у нас выйдет ошибка
print(student1['gender'])

# в случаях, когда мы не знаем, есть такой ключ или нет, мы можем использовать метод get
# этот метод вернёт знаение ключа, если такой ключ есть
# или None, если такого ключа нет
# либо вывести нужное нам сообщение
print(student1.get('gender', 'Такого ключа нет....')) # Такого ключа нет....


# как добавить элемент в список subjects в словаре student1?
# как обычно с помощью метода append
student1['subjects'].append('geometry')
print(student1)
# {'name': 'Mike', 'age': 16, 'subjects': ['bio', 'math', 'history', 'geometry'], 'contract': False}

# по списку внутри словаря можно пройтись циклом for
for s in student1['subjects']:
    print(s)
# bio
# math
# history
# geometry

# и изменять значение элемента, обращаясь по индексу:
student1['subjects'][0] = 'biology'
print(student1)
# {'name': 'Mike', 'age': 16, 'subjects': ['biology', 'math', 'history', 'geometry'], 'contract': False}
