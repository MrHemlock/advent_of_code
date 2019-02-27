from itertools import permutations

preferences = {}
group = []
best = 0

with open('input13.txt') as file:
    raw_data = [line.strip(".\n").split() for line in file.readlines()]

for line in raw_data:
    primary = line[0]
    secondary = line[-1]
    if line[2] == 'lose':
        units = int('-' + line[3])
    else:
        units = int(line[3])

    if primary not in preferences:
        preferences[primary] = {}
    preferences[primary][secondary] = units


seatings = [list(group) + [group[0]] for group in permutations(preferences.keys())]

for seating in seatings:
    total = sum([preferences[seating[i]][seating[i+1]] for i in range(len(seating)-1)])
    seating = seating[::-1]
    total += sum([preferences[seating[i]][seating[i+1]] for i in range(len(seating)-1)])
    if best < total:
        best = total


print(best)
