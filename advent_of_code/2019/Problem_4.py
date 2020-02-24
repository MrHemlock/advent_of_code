from intcode import process_instructions

with open("inputs/day_2_input.txt") as file:
    data = file.read().split(',')

clean_data = [*map(int, data)]

flag = False

for noun in range(100):
    for verb in range(100):
        clean_data[1], clean_data[2] = noun, verb
        result = process_instructions(clean_data[:])
        if result == 19690720:
            flag = True
            break
    if flag:
        break

print(100 * noun + verb)
