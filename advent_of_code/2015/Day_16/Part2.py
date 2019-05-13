sues = dict()
correct = None

REAL_SUE = {"children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1}


def value_checker(stats):
    for condition in stats:
        if condition in ("cats", "trees"):
            yield stats[condition] > REAL_SUE[condition]
        elif condition in ("pomeranians", "goldfish"):
            yield stats[condition] < REAL_SUE[condition]
        else:
            yield stats[condition] == REAL_SUE[condition]


with open("input16.txt", encoding="utf-8") as file:
    raw_data = [line.split() for line in file.readlines()]

# The data has colons and commas on some lines, we strip them away here
data = [[word.strip(':,') for word in line] for line in raw_data]

for line in data:
    sues[int(line[1])] = {line[2]: int(line[3]),
                          line[4]: int(line[5]),
                          line[6]: int(line[7])}

for key, values in sues.items():
    if all(value_checker(values)):
        correct = key
        break
print(correct)
