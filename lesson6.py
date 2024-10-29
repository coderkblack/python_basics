#list
scores = [90, 65, 34, 71, 55, 77, 89]

#access value
print(scores[0])#first
print(scores[2])#third

#add a number
scores.append(61)
print(scores)

#remove the last item
scores.pop()
print(scores)

#remove from index 3
scores.pop(3)
print(scores)

scores.sort(reverse=True)
print(scores)

print(len(scores))
