import numpy as np

clean_data = []
data = []
lights = np.full((1000, 1000), False, dtype=np.bool)

with open("input6.txt") as file:
    for line in file:
        data.append(line.split())


for line in data:
    temp_data = []
    if "turn" in line[0]:
        temp_data.append(line[1])
        temp_data.append([int(x) for x in line[2].split(',')])
        temp_data.append([int(x) for x in line[-1].split(',')])
    else:
        temp_data.append(line[0])
        temp_data.append([int(x) for x in line[1].split(',')])
        temp_data.append([int(x) for x in line[-1].split(',')])

    clean_data.append(temp_data)

for order in clean_data:
    if 'on' in order[0]:
        lights[order[1][0]:order[2][0]+1, order[1][1]:order[2][1]+1] = True
    elif 'off' in order[0]:
        lights[order[1][0]:order[2][0] + 1, order[1][1]:order[2][1] + 1] = False
    else:
        with np.nditer(
                lights[order[1][0]:order[2][0] + 1, order[1][1]:order[2][1] + 1],
                op_flags=['writeonly']
        ) as it:
            for x in it:
                x[...] = not x

unique, totals = np.unique(lights, return_counts=True)
print(unique)
print(totals)
