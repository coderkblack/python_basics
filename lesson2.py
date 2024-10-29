MAX_AGE = 30
MIN_AGE = 18

#variables
# store data -- variable, database
# manipulate data -- using operators, filtering the data
# display the data

#Storing data

#integer
age = 21
print(age)

#float
weight = 65.88
print(weight)

#string
name = 'Santa'
print(name)

#boolean
is_mature: bool = False

def mature():
    while True:
        new_age = input("Please enter your age: ")
        if new_age.isdigit():
            new_age = int(new_age)
            if MIN_AGE <= new_age <= MAX_AGE:
                break
            else:
                print("Failed")
        else:
            print("Please enter a number")
    return new_age


def main():
    current_age = mature()
    return current_age

main()


#camel casing
isMatureEnough = True

distance_to_the_sun = 400
print(f'The distance to the sun is {distance_to_the_sun} million kms')


