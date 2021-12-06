with open("Day_3_input.txt") as file:
    raw_data = [line.split() for line in file.readlines()]
    data = [(int(a), int(b), int(c)) for a, b, c in raw_data]

total = 0

for (a, b, c) in data:
    if (a + b > c) and (a + c > b) and (c + b > a):
        total += 1

print(total)
