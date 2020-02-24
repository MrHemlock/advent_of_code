from string import ascii_lowercase

data = "hepxxzaa"
bad_letters = "iol"
straights = set()
doubles = set((let * 2 for let in ascii_lowercase if let not in bad_letters))
cleaned_letters = tuple(let for let in ascii_lowercase if let not in bad_letters)
next_letter = dict(zip("abcdefghjkmnpqrstuvwxyz", "bcdefghjkmnpqrstuvwxyza"))


def increment_letters(code):
    if code[-1] == 'z':
        return increment_letters(code[:-1]) + 'a'
    else:
        return code[:-1] + next_letter[code[-1]]


for index in range(len(ascii_lowercase)-2):
    if not any((let in ascii_lowercase[index:index+3] for let in bad_letters)):
        straights.add(ascii_lowercase[index:index+3])

while True:

    # print(data)

    for i in range(len(data)-2):
        if data[i:i+3] in straights:
            break
    else:
        data = increment_letters(data)
        continue

    count = 0
    for i in range(len(data)-1):
        if data[i:i+2] in doubles and data[i:i+2] != data[i+1:i+3]:
            count += 1
        if count == 2:
            break
    else:
        data = increment_letters(data)
        continue

    break

print(data)
