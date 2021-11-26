with open("Day_1_input.csv") as file:
	parsed = file.read().strip().split(", ")

x = 0
y = 0
coords = set()
facing = 0
directions = [0, 0, 0, 0]
for step in parsed:
	if step[0] == "R":
		facing = (facing + 1) % 4
	else:
		facing = (facing - 1) % 4

	directions[facing] += int(step[1:])

	match facing:
		case 0:
			y += int(step[1:])
		case 1:
			x += int(step[1:])
		case 2:
			y -= int(step[1:])
		case 3:
			x -= int(step[1:])

	coord = (x, y)

	if coord in coords:
		print(sum(coord))
	coords.add(coord)

total = sum(directions[:2]) - sum(directions[2:])
print(total)
