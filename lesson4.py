#math functionality
import math

# value = input("Enter a number: ")
# value_square_root = math.sqrt(value)

x = 98
square_root = math.sqrt(x)
print('The root is', square_root)

rounded = round(square_root, 4)
print('The rounded square root is: ', rounded)

#functions
print('The content within a print function is an argument')
rounded2 = round(1.23456677888999098182, 5) #This is how we call the round function
print(rounded2) #This is how we call the print function

print(round(4.4444444445, 4))
print(math.sqrt(576))
print(math.pow(2, 6))
print('--------------------')
name = 'Jakes kaRiUki cHEge'
print(len(name))
print(name.lower())
print(name.upper())
print(name.title()) #Ensures each word starts with uppercase character with the rest being lower case.
print(name.capitalize()) #Ensures the sentence starts with an uppercase character

#Replacing words within a sentence
post = 'This is so easy and fluent'
new_post = post.replace('fluent', 'flowing')
print(new_post)

#if statements
#lists
#loops