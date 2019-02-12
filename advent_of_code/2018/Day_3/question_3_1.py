import numpy as np

clean_data = []
cloth = np.zeros((1000, 1000), dtype=int)

with open("input3.txt") as file:
    data = list(file)


for line in data:
    split_line = line.split()
    coords = split_line[2].split(",")
    length = split_line[3].split("x")
    x_y_pair = [int(coords[0]), int(length[0]), int(coords[1][:-1]), int(length[1])]
    clean_data.append(x_y_pair)

print(clean_data)

for x, x_len, y, y_len in clean_data:
    cloth[x:x+x_len, y:y+y_len] += 1

print(cloth)
unique, totals = np.unique(cloth, return_counts=True)
print(unique)
print(totals)
print(sum(totals[2:]))
