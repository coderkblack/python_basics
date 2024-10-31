first_name = input("What is your first name? ")
print("Hello", first_name)
#Branching with if, elif and else
if first_name == "Jakes":
    print(first_name, "is learning Python")
elif first_name == "Maximiliane":
    print(first_name, "is learning with fellow students in the community! Me too!")
else:
    #This is just in case we have a younger user who can't yet read
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow you're {}! If you're confident with your reading already...".format(age))
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}".format(first_name))
# for bool, any argument that is not empty returns True when called
# Truthy and Falsey -- emptiness is falsey
#   == --> Used for comparison, = --> Used for assigning

#1:37:25