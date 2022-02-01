class Avto:
    def __init__(self, price, name, color, brand):
        self.price = price
        self.name = name
        self.color = color
        self.brand = brand
        self.meter = 0
    def get_price(self):
        return self.price
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    def get_brand(self):
        return self.brand
    
    
    def get_info(self):
       print(f'{self.name} masinasining brendi {self.brand} rangi {self.color} narxi {self.price} ')

class Gm(Avto):
    def __init__(self, price, name, color, brand, tezlik):
        super().__init__(price, name, color, brand)
        self.tezlik = tezlik
        
    def get_tezlik(self):
        return self.tezlik
    def set_tezlik(self,qiymat):
        self.tezlik = qiymat
    def get_info(self):
       print(f'{self.name} masinasining brendi {self.brand} rangi {self.color} narxi {self.price} tezligi {self.tezlik}')
mashina = Gm(12000, 'cobalt', 'grey', 'chevrolet', '220')
mashina.set_tezlik(240)
mashina.get_info()
