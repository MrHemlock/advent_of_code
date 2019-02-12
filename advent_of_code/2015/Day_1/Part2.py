floor = 0

with open("input1.txt") as file:
    data = file.read()


for i, char in enumerate(data):
    if char == "(":
        floor += 1
    else:
        floor -= 1

    if floor < 0:
        print(i+1)
        break
