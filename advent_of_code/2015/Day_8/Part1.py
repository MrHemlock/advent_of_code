with open("input8.txt") as file:
    data = [line.strip() for line in file]

eval_data = [eval(line.strip()) for line in data]

data_total = sum([len(repr(line)) for line in data])
eval_total = sum([len(line) for line in eval_data])

print(data_total)

grand_total = data_total - eval_total
print(grand_total)
