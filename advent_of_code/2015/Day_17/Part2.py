from itertools import combinations

total = 0
totals = {}

with open("input17.txt") as file:
    containers = [int(jug) for jug in file]
print(containers)


for i in range(len(containers)):
    # for group in combinations(containers, (i+1)):
    totals[i+1] = sum(1 for group in combinations(containers, (i+1)) if sum(group) == 150)

print(totals)
