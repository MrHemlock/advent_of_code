houses_hit = set()
x = 0
y = 0

with open("input3.txt") as file:
    data = file.read()

houses_hit.add((x, y))
for char in data:
    if char == "v":
        y -= 1
    elif char == ">":
        x += 1
    elif char == "<":
        x -= 1
    else:
        y += 1
    houses_hit.add((x, y))

print(houses_hit)
print(len(houses_hit))
