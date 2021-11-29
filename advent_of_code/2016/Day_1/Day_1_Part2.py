with open("Day_1_input.txt") as file:
	parsed = file.read().strip().split(", ")

x = 0
y = 0
coords = set((0,0))
facing = 0
finished = False
for step in parsed:
	if step[0] == "R":
		facing = (facing + 1) % 4
	else:
		facing = (facing - 1) % 4

	for _ in range(int(step[1:])):
		match facing:
			case 0:
				y += 1
			case 1:
				x += 1
			case 2:
				y -= 1
			case 3:
				x -= 1

		coord = (x, y)

		if coord in coords:
			print(abs(x) + abs(y))
			finished = True
			break

		coords.add(coord)

	if finished:
		break
