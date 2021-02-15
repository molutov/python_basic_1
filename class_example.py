class Person:
  def __init__(example, name, age):
    example.name = name
    example.age = age
  def welcome(example):
    print("Hello " + example.name)
p1 = Person("Bekzat", 18)
p1.welcome()
