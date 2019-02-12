import numpy as np

clean_data = []
data = []
lights = np.zeros((1000, 1000), dtype=np.int)

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
        lights[order[1][0]:order[2][0] + 1, order[1][1]:order[2][1] + 1] += 1
    elif 'off' in order[0]:
        with np.nditer(
                 lights[order[1][0]:order[2][0] + 1, order[1][1]:order[2][1] + 1],
                 op_flags=['readwrite']
        ) as it:
            for x in it:
                if x > 0:
                    x[...] -= 1
    else:
        lights[order[1][0]:order[2][0] + 1, order[1][1]:order[2][1] + 1] += 2


print(lights.sum())