# by Bekzat
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def welcome(self):
    print("Hello " + self.name)
        
p1 = Person("Beka", 18)
p1.welcome()