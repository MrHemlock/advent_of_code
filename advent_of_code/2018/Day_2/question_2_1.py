doubles = 0
triples = 0
letters = None
dub_flag = False
trip_flag = False

with open('input2.txt') as file:
    for line in file:
        letters = set(line)
        for letter in letters:
            if line.count(letter) == 2 and not dub_flag:
                dub_flag = True
                doubles += 1
            elif line.count(letter) == 3 and not trip_flag:
                trip_flag = True
                triples += 1
        dub_flag = False
        trip_flag = False

print(triples * doubles)
