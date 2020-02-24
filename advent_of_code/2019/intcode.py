from itertools import islice
from math import prod
from typing import List


def process_instructions(instructions: List[int]) -> int:
    i = 0
    for opcode in islice(instructions, 0, None, 4):
        inputs = instructions[instructions[i + 1]], instructions[instructions[i + 2]]
        output_location = instructions[i + 3]
        if opcode == 1:
            instructions[output_location] = sum(inputs)
        elif opcode == 2:
            instructions[output_location] = prod(inputs)
        elif opcode == 99:
            break
        else:
            raise Exception("Should never get here")
        i += 4
    return instructions[0]
