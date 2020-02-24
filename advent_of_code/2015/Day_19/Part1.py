combos = {}
molecules = set()

with open("input19.txt") as file:
    for line in file:
        separated = line.strip().split()
        if separated[0] not in combos:
            combos[separated[0]] = []
        combos[separated[0]].append(separated[2])

with open("input19_2.txt") as file:
    base = file.read().strip()

for i, let in enumerate(base):
    if let in combos:
        for swap in combos[let]:
            molecules.update([f"{base[:i]}{swap}{base[i + 1:]}"])
    elif base[i:i+2] in combos:
        for swap in combos[base[i:i+2]]:
            molecules.update([f"{base[:i]}{swap}{base[i+2:]}"])
print(len(molecules))
print(combos)
