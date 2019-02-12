houses_hit = set()
santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0

with open("input3.txt") as file:
    data = file.read()

houses_hit.add((0, 0))
for i, char in enumerate(data):
    if i % 2 == 0:
        if char == "v":
            santa_y -= 1
        elif char == ">":
            santa_x += 1
        elif char == "<":
            santa_x -= 1
        else:
            santa_y += 1
        houses_hit.add((santa_x, santa_y))
    else:
        if char == "v":
            robo_y -= 1
        elif char == ">":
            robo_x += 1
        elif char == "<":
            robo_x -= 1
        else:
            robo_y += 1
        houses_hit.add((robo_x, robo_y))

print(houses_hit)
print(len(houses_hit))
