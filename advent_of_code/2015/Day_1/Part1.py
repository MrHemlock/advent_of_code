floor = 0

with open("input1.txt") as file:
    data = file.read()

print(data)

for char in data:
    if char == "(":
        floor += 1
    else:
        floor -= 1

print(floor)
