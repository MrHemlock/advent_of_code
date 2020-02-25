from input_getter import get_input

DIRECTION_STRING = "RULD"
wires = [set(), set()]

get_input(3)
with open("inputs/day_3_input.txt") as file:
    data = [line.split(",") for line in file]

direction_dict = {let: (1 + 0j) * (1j ** i) for (let, i) in zip(DIRECTION_STRING, range(4))}

for wire, directions in zip(wires, data):
    x = 0
    y = 0
    for direction in directions:
        amount = int(direction[1:])
        x_mask = direction_dict[direction[0]].real
        y_mask = direction_dict[direction[0]].imag
        coords = [(x + (x_mask * i), y + (y_mask * i))
                  for i in range(1, amount + 1)
                  if (x + (x_mask * i), y + (y_mask * i)) not in wire]
        x += amount * x_mask
        y += amount * y_mask
        wire.update(coords)

wire_crossing = wires[0] & wires[1]
distance = min([abs(x) + abs(y) for (x, y) in wire_crossing])
print(distance)
