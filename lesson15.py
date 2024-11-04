# inheritance
# erroe Handling
# dates
# overriding
# abstraction
from datetime import datetime, date

from lesson17 import date_of_birth


class Employee:
    def __init__(self, name, id_number, dob, gender):
        self.name = name
        self.id_number = id_number
        self.dob = dob
        self.gender = gender
        date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
        self.age = date.today().year - date_of_birth.year

    def print_details(self):
        print(f"Name: {self.name}\nID Number: {self.id_number}\nDOB: {self.dob}\nGender: {self.gender}\nAge: {self.age}")


# Child class
class PermanentEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, salary):
        super().__init__(name, id_number, dob, gender)  # calling the functions from the parent class
        self.salary = salary

    def print_salary(self):
        print(f"Salary is {self.salary}")

    def print_details(self):#to override implies that if a function appears in both the child and parent class, the one in the child will be considered
        super().print_details()
        print(f"Salary is {self.salary}")


class TemporaryEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, hourly_pay, end_date):
        super().__init__(name, id_number, dob, gender)
        self.hourly_pay = hourly_pay
        self.end_date = end_date

    def print_hourly_pay(self):
        print(f"Hourly payment is {self.hourly_pay}")

    def print_end_date(self):
        print(f"End date is {self.end_date}")

p1 = PermanentEmployee(name="John Mark", id_number="1023456", gender="M", dob="1990-01-26", salary=10000)
p1.print_details()
p1.print_salary()

t1 = TemporaryEmployee("Jim ", "21345678", "1995-11-12", "M", 1000, "2024-12-23")
t1.print_details()

