# by Bekzat
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    def welcome(self):
        print(self.first_name, self.last_name)
p1 = Person("Bekzat", "Molutov")
p1.welcome()
