from itertools import islice
from math import prod

from input_getter import get_input


get_input(2)
with open("inputs/day_2_input.txt") as file:
    data = file.read().split(',')

clean_data = [*map(int, data)]

clean_data[1] = 12
clean_data[2] = 2
i = 0

for opcode in islice(clean_data, 0, None, 4):
    inputs = clean_data[clean_data[i+1]], clean_data[clean_data[i+2]]
    output_location = clean_data[i+3]
    if opcode == 1:
        clean_data[output_location] = sum(inputs)
    elif opcode == 2:
        clean_data[output_location] = prod(inputs)
    elif opcode == 99:
        break
    else:
        raise Exception("Should never get here")
    i += 4

print(clean_data[0])
