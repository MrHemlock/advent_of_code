import numpy as np

best = 0


def product(num):
    if len(num) == 1:
        return num[0]
    return num[0] * product(num[1:])


def amounts():
    for i in range(101):
        for j in range(101 - i):
            for k in range(101 - (i + j)):
                l = 100 - (i + j + k)
                yield np.array([i, j, k, l], dtype=np.int32)


with open("input15.txt", encoding="utf-8") as file:
    raw_data = [line.split() for line in file.readlines()]

# The data has colons and commas on some lines, we strip them away here
data = [[word.strip(':,') for word in line] for line in raw_data]

# The numbers that we need are still strings, so we pick them out and convert them
numbers = np.array([[int(x) for x in group[2:-1:2]] for group in data], dtype=np.int32)

for group in amounts():
    numbers_copy = np.copy(numbers)
    for i, (pair) in enumerate(zip(numbers_copy, group)):
        # print(pair)
        # print(pair[0] * pair[1])
        numbers_copy[i] = pair[0] * pair[1]

    summed = []
    for column in numbers_copy.T:
        temp = np.sum(column)
        if temp < 0:
            temp = 0
        summed.append(temp)
    score = product(summed)
    if score > best:
        best = score
    print(score)
    # print(numbers_copy)
print(best)

# for pair in zip(numbers_array, test):
#     print(pair)
#     print(pair[0] * pair[1])
