# import pandas as pd
#
# #loops
# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")
#
# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")
#
# #Nested loops
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")
#
# #range object is iterable, iterable objects can be used in the for loop
# #Othe iterable objects include strings, lists
# print(type(range(5)))
#
# for x in "Python":
#     print(x)
#
# for i in [1, 2, 3, 4, 5]:
#     print(i)
#
# for number in range(2, 10, 2):
#     print(number)
# print("We have 4 even numbers")
#
# for number in range(1, 10):
#     if number % 2 == 0:
#         print(number)
# print("We have 4 even numbers")
#
# user_details_list = []
# for number in range(1, 3):
#     user_details = {"name": input("What is your name? "),
#                   "school": input("What is your school? "),
#                   "course": input("What is your course? "),
#                 "Academic Year": input("What is your Academic Year? ")}
#     user_details_list.append(user_details)
# print(user_details_list)
#
# df = pd.DataFrame(user_details_list)
# print(df)

import tkinter as tk
from tkinter import messagebox

# Function to collect user details and store them in a dictionary
def collect_details():
    user_details = {
        "name": name_entry.get(),
        "school": school_entry.get(),
        "course": course_entry.get(),
        "Academic Year": year_entry.get()
    }
    user_details_list.append(user_details)
    messagebox.showinfo("Info", "Details added successfully!")
    clear_entries()

# Function to clear the entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    school_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("User Details Form")

# Create a list to store user details
user_details_list = []

# Create and place labels and entry widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="School:").grid(row=1, column=0, padx=10, pady=5)
school_entry = tk.Entry(root)
school_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Course:").grid(row=2, column=0, padx=10, pady=5)
course_entry = tk.Entry(root)
course_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Academic Year:").grid(row=3, column=0, padx=10, pady=5)
year_entry = tk.Entry(root)
year_entry.grid(row=3, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=collect_details)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()

# Print the collected user details
print(user_details_list)
