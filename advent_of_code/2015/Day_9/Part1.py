from itertools import permutations

cities = {}
best = None

with open('input9.txt') as file:
    raw_data = [line.split() for line in file]

for group in raw_data:
    if group[0] not in cities:
        cities[group[0]] = {}
    if group[2] not in cities:
        cities[group[2]] = {}
    cities[group[0]][group[2]] = int(group[-1])
    cities[group[2]][group[0]] = int(group[-1])

groupings = [group for group in permutations(cities.keys())]

for group in groupings:
    total = 0
    for index in range(len(group)-1):
        total += cities[group[index]][group[index+1]]
    if best is None or best > total:
        best = total
print(best)
