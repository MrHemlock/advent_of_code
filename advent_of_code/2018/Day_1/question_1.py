total = 0
with open('input1.txt') as file:
    for num in file:
        total += int(num)
print(total)
