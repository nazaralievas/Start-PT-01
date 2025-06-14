# Разбор домашки:
# Есть данные о книге:
book = {"author": "Bill Smith",
        'genre': ['adventure', 'comedy'],
        "title": "Blue Cat",
        "price": 450,
        "sales": 1500}

# Снизьте стоимость книги на 20%
book["price"] = book["price"] * 0.8

# к списку genre добавьте 'kids'
book['genre'].append('kids')

# Добавьте ещё один ключ "best_seller", со значением True
book['best_seller'] = True

print(book)
# {'author': 'Bill Smith', 'genre': ['adventure', 'comedy', 'kids'], 'title': 'Blue Cat', 'price': 360.0, 'sales': 1500, 'best_seller': True}

# ---------------------------------------------


# в словаре student1 значением ключа 'subjects' является список ['bio', 'math', 'history']
student1 = {
    'name': 'Mike',
    'age': 16,
    'subjects': ['bio', 'math', 'history']}

# однако, удобнее было бы вместо списка использовать словарь, в котором ключами будут названия предметов, а значениями оценки:
student1 = {
    'name': 'Mike',
    'age': 16,
    'subjects': {'bio': 3, 'math': 4, 'history': 4}}

# теперь значение ключа subjects выглядит вот так:
print(student1['subjects']) # {'bio': 3, 'math': 4, 'history': 4}

# оценку за математику можем узнать с помощью ключа:
print(student1['subjects']['math']) # 4

# поменяем оценку за биологию:
student1['subjects']['bio'] = 5

# проверим оценки:
print(student1['subjects']) # {'bio': 5, 'math': 4, 'history': 4}


# в словаре database хранятся данные о двух студентах под ключами 1 и 2
database = {
        1: {
    'name': 'Mike',
    'age': 16,
    'subjects': {'bio': 3,
                 'math': 4,
                 'history': 4},
    'contract': False
        },
        2: {
    'name': 'Rose',
    'age': 17,
    'subjects': {'bio': 4,
                 'math': 4,
                 'history': 3},
    'contract': True
        }
}
# выведем оценку за историю у второго студента:
print(database[2]['subjects']['history']) # 3

# поменяем эту оценку на 4
database[2]['subjects']['history'] = 4

# теперь у второго студента за историю стоит четвёрка:
print(database[2]['subjects']['history']) # 4


# добавим первому студенту ещё один предмет географию со значением 5
database[1]['subjects']['geography'] = 5

# ---------------------------------------------------

# рассмтрим методы словарей
grades = {
    'biology': 4,
    'chemistry': 4,
    'math': 3,
    'GE': 5,
    'physics': 4,
    'history': 5
}
# с помощью метода keys() мы можемм вывесли все ключи:
print(grades.keys()) # dict_keys(['biology', 'chemistry', 'math', 'GE', 'physics', 'history'])

# с помощью метода values() мы можем вывести все значения:
print(grades.values()) # dict_values([4, 4, 3, 5, 4, 5])
# так как в значениях одни числа, попробуем применить к ним функцию sum
print(sum(grades.values())) # 25
# и функцию len
print(len(grades.values())) # 6
# используя эти две функции посчитаем средний балл за все предметы:
average = sum(grades.values()) / len(grades.values())
print(average) # 4.166666666666667

# давайте округлим average с помощью функции round. Если применить просто round, то он округлит до целого числа:
print(round(average)) # 4
# если передать параметр, например 1, то округлит до 1 цифры после точки
print(round(average, 1)) # 4.2
print(round(average, 2)) # 4.17


# вспомним метод count, который считает количество вхождений элемента в списке
# с помощью него посчитаем сколько раз каждый президент встречается в списке votes
votes = ["Trump", "Biden", "Trump", "Biden", "Trump", "Trump", "Bush"]
print(votes.count('Trump')) # 4
print(votes.count('Biden')) # 2
print(votes.count('Bush')) # 1


# давайте посчитайем количество голосов с помощью цикла с созданием такого словаря {'Trump': 4, 'Biden': 2, 'Bush': 1}
votes = ["Trump", "Biden", "Trump", "Biden", "Trump", "Trump", "Bush"]
results = {}
for candidate in votes:
    results[candidate] = votes.count(candidate)

print(results) # {'Trump': 4, 'Biden': 2, 'Bush': 1}


# такой словарь можно получить с помощью dictionary comprehension:
votes = ["Trump", "Biden", "Trump", "Biden", "Trump", "Trump", "Bush"]
results = {candidate: votes.count(candidate) for candidate in votes}
print(results) # {'Trump': 4, 'Biden': 2, 'Bush': 1}


# задача: получить словарь, в котором ключами будут символы из строки text, а значениями будут количество этого символа в тексте
# вот так: {'Ш': 1, 'л': 1, 'а': 2..........}
# решение с помощью цикла:
text = 'Шла Саша по шоссе'
kolich_bukv = {}
for b in text:
    kolich_bukv[b] = text.count(b)

print(kolich_bukv)
# {'Ш': 1, 'л': 1, 'а': 3, ' ': 3, 'С': 1, 'ш': 2, 'п': 1, 'о': 2, 'с': 2, 'е': 1}


# решение с помощью dictionary comprehension
text = 'Шла Саша по шоссе'
kolich_bukv = {b: text.count(b) for b in text}
print(kolich_bukv)
# {'Ш': 1, 'л': 1, 'а': 3, ' ': 3, 'С': 1, 'ш': 2, 'п': 1, 'о': 2, 'с': 2, 'е': 1}

