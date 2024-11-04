#functions
#area for ten triangles
import math
from datetime import date

t1 = 0.5 * 10 * 12
print(t1)


def calc_area_triangle(b, h):
    area = 0.5 * b * h
    area = round(area, 2)
    print(area)

def calc_area_circle(radius):
    area = math.pi * radius * radius
    area = round(area, 2)
    print(f"The area of the circle is {area} cm^2")

def print_todays_date():
    today = date.today()
    print(today)

def add(*args):
    total = 0
    for num in args:
        total += num
    print(f"The total is {total}")

def sayHi(name, age=21):
    print(f"Hello {name}, I am {age} years old.")

sayHi("John")
sayHi("Kevo", 23)

sayHi(name="Kevin", age=23)#this enables us to switch the arguments 

users = ["A", "B", "C"]
users.sort(reverse=True)

#use a function == calling
calc_area_triangle(12, 10)
#Nested list
triangles = [[12, 16], [8, 9], [6, 13], [21, 27], [61, 14], [31.5, 66.97]]

for t in triangles:
    calc_area_triangle(t[0], t[1])

calc_area_circle(2.76)
calc_area_circle(0.5)

print_todays_date()

add(1, 2)
add(7, 8, 9)
add(123456, 78920, 1112131415, 23456789, 12, 23, 45, 6789)

#data -- name, phone, gender
#Account -- deposit, withdrawal, check balance, service charge
#Object oriented programming comes in handy
#----------------------------------------
#matatu system --> number plate, driver, conductor, route
#We create a class matatu