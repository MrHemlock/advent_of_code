with open("Day_1_input.csv") as file:
	parsed = file.read().strip().split(", ")


facing = 0
directions = [0, 0, 0, 0]
for step in parsed:
	if step[0] == "R":
		facing = (facing + 1) % 4
	else:
		facing = (facing - 1) % 4

	directions[facing] += int(step[1:])

total = sum(directions[:2]) - sum(directions[2:])
print(total)
