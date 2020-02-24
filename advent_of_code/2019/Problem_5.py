from input_getter import get_input


wires = [set(), set()]

get_input(3)
with open("inputs/day_3_input.txt") as file:
    data = [line.split(",") for line in file]

for wire, directions in zip(wires, data):
    x = 0
    y = 0
    for direction in directions:
        amount = int(direction[1:])
        if direction[0] == "R":
            coords = [(x + i, y) for i in range(1, amount + 1) if (x + i, y) not in wire]
            x += amount
        elif direction[0] == "U":
            coords = [(x, y + i) for i in range(1, amount + 1) if (x, y + i) not in wire]
            y += amount
        elif direction[0] == "L":
            coords = [(x - i, y) for i in range(1, amount + 1) if (x - i, y) not in wire]
            x -= amount
        else:
            coords = [(x, y - i) for i in range(1, amount + 1) if (x, y - i) not in wire]
            y -= amount

        wire.update(coords)

wire_crossing = wires[0].intersection(wires[1])

distances = [abs(j) + abs(k) for (j, k) in wire_crossing]

print(min(distances))
