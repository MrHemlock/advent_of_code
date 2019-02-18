total = 0

with open("input8.txt") as file:
    data = [line.strip() for line in file]


new_data = [repr(line) for line in data]


new_data_total = sum([len(repr(line)) for line in data])
data_total = sum(len(line) for line in new_data)

# print(f"{new_data_total - data_total}")


for line in data:
    total += 6
    for char in line:

        if char in ("\\", '"', "'"):
            total += 2
        else:
            total += 1

print(f"{total - data_total}")
