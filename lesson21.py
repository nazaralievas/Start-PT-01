# так как классы Таксист, Клиент и Курьер обладают одинаковыми атрибутами:
# id, имя, номер телефона
# можно наследовать эти три класса от общего родительского класса Person
class Person:
    def __init__(self, id, name, phone_num):
        self.id = id
        self.name = name
        self.phone_num = phone_num

    def __str__(self):
        return f'Имя: {self.name}. Номер телефона: {self.phone_num}'


# классы Клиент и Курьер наследуют все атрибуты и методы родителя, поэтому
# для создания этих классов достаточно:
class Client(Person):
    pass

class Courier(Person):
    pass

# и уже можно создавать объекты этих классов:
courier_1 = Courier(1, 'Tom', '+908765')
# и пользоваться методом __str__ родительского класса:
print(courier_1) # Имя: Tom. Номер телефона: +908765


client_1 = Client(1, 'Saadat', '07765435')
print(client_1) # Имя: Saadat. Номер телефона: 07765435


# а вот класс Таксист имеет несколько своих атрибутов, которых нет у родителя:
# номер машины, марка машины, рейтинг и стаж
# поэтому наследование тут выглядит так:
class Taxist(Person):
    def __init__(self, id, name, phone_num, car_num, car_model, rating, staj):
        super().__init__(id, name, phone_num) # super ссылается на родителя, то ест у родителя мы наследуем id, name, phone_num
        self.car_num = car_num # а всё остальное как обычно
        self.car_model = car_model
        self.rating = rating
        self.staj = staj

    # и метод __str__ у Таксиста изменён:
    def __str__(self):
        return f'Водитель: {self.name}, машина: {self.car_model}, номер авто: {self.car_num}'

    # а так же  есть свой собственный метод get_staj
    def get_staj(self):
        from datetime import datetime
        year = datetime.now().year
        return year - self.staj


# создадим объект класса Таксист
taxist_1 = Taxist(1, 'Айбек', '+996778000012', 'X007AN', 'BMW 6', 4, 1999)


# и наконец напишем класс Поездка, где будет храниться информация о поездке:
class Poezdka:
    def __init__(self, id, marshrut, time_start, stoimost, client, taxist):
        self.id = id
        self.marshrut = marshrut
        self.time_start = time_start
        self.stoimost = stoimost
        self.client = client
        self.taxist = taxist

# создавая объект класса Поездка, мы могли бы написать так:
poezdka_1 = Poezdka(1, 'Codify-BishkekPark', '15:01', 340, 'Саадат', 'Айбек')

# но ведь у нас уже есть объекты классов Клиент и Таксист:
taxist_1 = Taxist(1, 'Айбек', '+996778000012', 'X007AN', 'BMW 6', 4, 1999)
client_1 = Client(1, 'Саадат', '07765435')

# мы можем эти объекты (экземпляры) класса использовать в виду атрибутов объекта poezdka_1
poezdka_1 = Poezdka(1, 'Codify-BishkekPark', '15:01', 340, client_1, taxist_1)

print(poezdka_1.client) # Имя: Саадат. Номер телефона: 07765435
print(poezdka_1.taxist) # Водитель: Айбек, машина: BMW 6, номер авто: X007AN
print(poezdka_1.taxist.get_staj()) # 26
