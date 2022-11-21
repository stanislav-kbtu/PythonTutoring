class Human():
    
    teeth_count = 32

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city_from = city

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def CityAndName(self):
        return self.city_from + self.name

    def setTeethCount(self, n):
        self.teeth_count = n

    def __add__(self, human2):
        new = Human(self.name + human2.name, self.age + human2.age, self.city_from)
        return new

    def __sub__(self, human2):
        new = Human(human2.name, self.age - human2.age, human2.city_from)
        return new

class Asian(Human):

    def __init__(self, name, age, city, manner):
        Human.__init__(self, name, age, city)
        self.manner = manner

    def openEyes(self):
        return f'{self} has opened his eyes'

Stas = Human("Stanislav", 18, 'Atyrau')

Miras = Asian("Miras", 19, "Almaty", 'Rude')

print(type(Stas), type(Miras))

print(Stas.openEyes())