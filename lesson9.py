#loop
while True:
    print("Hello, loops")
    break

scores = [98, 76,56, 81, 78, 99, 54, 78, 66, 87, 90, 72, 64, 56, 78, 89, 67, 45, 80]

def case1(): #students who scored between 60 and 75
    for i in scores:
        if 60 <= i <= 75 and i % 2 == 0:
            print(i)

case1()