import re

compiled = re.compile(r"-?\d+")

with open("input12.json") as file:
    data = file.read()

numbers = compiled.findall(data)

total = sum([int(num) for num in numbers])
print(total)

print(data)
