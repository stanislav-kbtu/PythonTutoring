# parameter - VariableName.ParameterName
# function - VariableName.FunctionName()
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


Stas = Human("Stanislav", 17, 'Atyrau')

Miras = Human("Miras", 19, "Almaty")

print(Miras.setTeethCount(34))
print(Miras.teeth_count)


New = Stas + Miras
print(New.name, New.age)
New2 = Stas - Miras
print(New2.name, New2.age)
