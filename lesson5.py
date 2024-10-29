# if statements
# store data in lists, tuple, dictionary, set
# loops

# if statements
while True:
    score = input("Enter your score: ")
    if score.isdigit():
        score = int(score)
        if score > 0:
            break
        else:
            print("Score must be greater than 0.")
    else:
        print("Enter a number")

# elif not score.isdigit():
#     print("Please enter a number")
#     exit(0) #stop

if score >= 78:
    print("A")
elif 71 <= score <= 78:  # score >= 71 and score <= 77
    print("A-")
elif 64 <= score <= 70:  # score >= 64 and score <= 70
    print("B+")
elif 57 <= score <= 63:  # score >= 57 and score <= 63
    print("B")
elif 50 <= score <= 56:  # score >= 50 and score <= 56
    print("B-")
elif 43 <= score <= 49:  # score >= 43 and score <= 49
    print("C+")
elif 36 <= score <= 42:  # score >= 36 and score <= 42
    print("C")
elif 29 <= score <= 35:  # score >= 29 and score <= 35
    print("C-")
elif 22 <= score <= 28:  # score >= 22 and score <= 28
    print("D+")
elif 15 <= score <= 21:  # score >= 15 and score <= 21
    print("D")
elif 8 <= score <= 14:  # score >= 8 and score <= 14
    print("D-")
else:
    print("E")

score2 = int(input("Enter your score: "))
grades = [(78, "A"), (71, "A-"), (64, "B+"), (57, "B"),
          (50, "B-"), (43, "C+"), (36, "C"), (29, "C"),
          (22, "C-"), (15, "D+"), (8, "D")]

for boundary, grade in grades:
    if grade >= boundary:
        print(grade)
        break
    else:
        print("E")
