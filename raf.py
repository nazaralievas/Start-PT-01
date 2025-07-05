class Taxist:
    def __init__(self, id, name, car_model):
        self.id = id
        self.name = name
        self.car_model = car_model
    
    def __str__(self):
        return f'Имя: {self.name}, Марка машины: {self.car_model}'

taxist1 = Taxist(1, 'Robert', 'Honda Fit')
print(taxist1)


class Client:
    def __init__(self, id, name, phone_num):
        self.id = id
        self.name = name
        self.phone_num = phone_num
    
    def __str__(self):
        return f'Имя: {self.name},Номер телефона: {self.phone_num} '

client1 = Client(1, 'Saadat', '+9967748545475497')
print(client1)


class Corier(Client):
    pass

corier1 = Corier(1, 'David', '+700564869')
print(corier1)