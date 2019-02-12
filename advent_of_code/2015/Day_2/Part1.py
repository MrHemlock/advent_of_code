cleaned_list = []
total = 0

with open("input2.txt") as file:
    data = file.readlines()


for grouping in data:
    temp = grouping.split('x')
    cleaned_list.append(sorted([int(i) for i in temp]))

total = sum([2*l*w + 2*w*h + 2*h*l + l*h for l, h, w in cleaned_list])

print(total)
