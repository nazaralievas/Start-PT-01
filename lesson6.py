# разберём домашку, которая звучата так:
# Напишите программу, которая по введенным длинам сторон треугольника определяет,
# является ли он равносторонним, равнобедренным или разносторонним.
# (Сначала проверьте, может ли существовать треугольник с такими сторонами, как мы делали на уроке.)

# Пояснение:
# Равносторонний — все стороны равны.
# Равнобедренный — любые две стороны равны.
# Разносторонний — все стороны разные.
 
a = 10
b = 12
c = 10
if a + b <= c or a + c <= b or b + c <= a: # проверяем может ли треугольник с заданными параметрами существовать
    print('Нет, такого треугольника быть не может')
else:
    if a == b == c: # если все три стороны равны
        print('Треугольник равносторонний')
    elif a == b or a == c or c == b: # если любые две стороны равны
        print('Треугольник равнобедреный')
    else: # если треугольник не равносторонний и не равнобедренный, значит:
        print('Треугольник раЗносторонний')


# сегодняшняя тема - цикл while
# while переводится как "пока"
# напишем код, который запрашивает у пользователя ввод пароля до тех пор ПОКА он не введёт верный пароль
password = input('Введите пароль: ')
while password != 'qwerty1': # пока введённый пароль не равен правильному ('qwerty1')
    password = input('Введите пароль cнова: ') # будет запрашиваться ввод пароля

# эти две строки кода будут воспроизводиться снова и снова пока пользователь не введёт верный пароль
# как только правильный пароль введён, может быть прочитан этот принт:
print('Тут банковские данные')


# задание 1
# загадайте число от 1 до 10
secret_num = 7
# и запрашивайте у пользователя число до тех пор, пока он не угадает это число
num = int(input('Угадайте число от 1 до 10: '))
while num != secret_num:
    num = int(input('Попробуйте снова: '))

print('Вы угадали!')


# то же задание, но теперь число будет загадывать сам питон с помощью модуля random
# модули в питоне можно представить в виде ящиков с инструментами
# для того чтобы получить доступ к модулю, нужно этот модуль импортировать в наш файл:
import random
# в модуле random есть функция randint, который выдает рандомное число в указанном диапозоне (от 1 до 10)
secret_num = random.randint(1, 10)
# дальнейший код выглядит так же как в предыдущем задании:
num = int(input('Угадайте число от 1 до 10: '))
while num != secret_num:
    num = int(input('Попробуйте снова: '))

print('Вы угадали!')


# давайте улучшим нашу программу - будем считать за какое количество попыток пользователь угадал число
secret_num = random.randint(1, 10)
num = int(input('Угадайте число от 1 до 10: ')) # пользователь уже попытался угадать число
# поэтому переменная popytki будет равно 1
popytki = 1
while num != secret_num: # пока пользователь не угадал загаданное число
    num = int(input('Попробуйте снова: ')) # запрашиваем у него число
    popytki = popytki + 1 # и количество попыток увеличиваем на 1

# когда он угадает число, мы выведем сообщение:
print(f'Вы угадали! Было загадано число {secret_num}. Вы угадали с {popytki} попытки!')


# цикл while можно использовать для вывода чисел ОТ и ДО какого либо числа
# давайте выведем числа от 1 до 10
# пишем: начиная с 1 принтуй число ПОКА число меньше 11 и после принта увеличивай число на 1
num = 1
while num < 11:
    print(num)
    num = num + 1

# в терминале увидим:
1
2
3
4
5
6
7
8
9
10

# когда num будет равно 10, к нему прибавится единица и получится 11
# условие while num < 11 будет False и цикл завершится


# давайте теперь выведем не просто числа от 1 до 10 а квадрад этих чисел:
num = 1
while num < 11:
    print(num ** 2)
    num = num + 1


# теперь давайте выведем числа от 10 до 1 по убыванию
num = 10
while num > 0:
    print(num)
    num = num - 1

# в терминале увидим:
10
9
8
7
6
5
4
3
2
1

# давайте теперь не просто выведем числа от 10 до 1, но и посчитаем сумму этих чисел
num = 10
summa = 0 # зададим переменную, куда будем складывать все числа
while num > 0:
    print(num)
    summa = summa + num
    num -= 1 # это сокращенная запись num = num - 1
print(summa)


# другое задание: выведите чётные числа от 2 до 100
num = 2  # стартовая точка 2, так как это первое чётное число
while num <= 100:
    print(num)
    num = num + 2 # будем прибавлять не по 1, а по два. Таким образом выведем все чётные числа от 2 до 100
