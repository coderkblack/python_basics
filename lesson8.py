import pandas as pd

#Dictionary {} -- storing key, value pairs
#list [], tuple ()
student = {"name": ("Jane Sarah", "James Musyoka"),
           "id": (1234, 5678),
           "age": (21, 23),
           "email": ("janesarah@gmail.com", "jamesyoka@gmail.com"),
           "gender": ("Female", "Male")}

print(student["name"])

student["Weight"] = (61, 70)
print(student)

#Set -- Does not allow a value to be repeated -- You can use it to remove duplicates from your data
#A set is unordered
people = {"Jane", "Bill", "Jane", "Kevo"}
print(people)

print(len(people))
people.discard("Kevo")
print(people)
# df = pd.DataFrame(student)
# print(df)