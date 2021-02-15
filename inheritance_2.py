# by Bekzat
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    def welcome(self):
        print(self.first_name, self.last_name)

class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname) # inheritance
        super().__init__(fname, lname) # inheritance
        self.graduation_year = 2024
        self.year_of_birth = year

# p1 = Person("Bekzat", "Molutov")
p2 = Student("Karim", "Renno", 2002)
# p1.welcome()
p2.welcome()
print("Graduation year:", p2.graduation_year)
print("Year of birth:", p2.year_of_birth)
