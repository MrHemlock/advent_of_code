with open("Day_3_input.txt") as file:
    raw_data = [line.split() for line in file.readlines()]
    data = [(int(a), int(b), int(c)) for a, b, c in raw_data]

total = 0


for i in range(0, len(data), 3):
    first = data[i]
    second = data[i+1]
    third = data[i+2]

    for j in range(3):
        if (first[j] + second[j] > third[j]) and (first[j] + third[j] > second[j]) and (second[j] + third[j] > first[j]):
            total += 1

print(total)
