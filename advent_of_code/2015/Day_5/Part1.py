from string import ascii_lowercase

NAUGHTY_COMBOS = ("ab", "cd", "pq", "xy")
VOWELS = "aeiou"
nice_total = 0
letter_doubles = tuple(x*2 for x in ascii_lowercase)

with open("input5.txt") as file:
    for line in file:
        if any(bad in line for bad in NAUGHTY_COMBOS):
            continue
        if sum(line.count(let) for let in VOWELS) < 3:
            continue
        if any(good in line for good in letter_doubles):
            nice_total += 1
print(nice_total)
