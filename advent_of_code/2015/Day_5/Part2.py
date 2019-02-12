from string import ascii_lowercase

DOUBLE_LETTERS = tuple(x+y for x in ascii_lowercase for y in ascii_lowercase)
SANDWICH_LETTERS = tuple(x+y+x for x in ascii_lowercase for y in ascii_lowercase)
nice_total = 0

with open("input5.txt") as file:
    for line in file:
        if any(line.count(dub) >= 2 for dub in DOUBLE_LETTERS):
            if any(line.count(let * 3) == 1 for let in ascii_lowercase):
                continue
        else:
            continue

        if any(sandwich in line for sandwich in SANDWICH_LETTERS):
            nice_total += 1

print(nice_total)
