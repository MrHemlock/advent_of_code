line1 = None
line2 = None
not_match_total = 0

with open('input2.txt') as file:
    text = list(file)

for i, line in enumerate(text):
    for j, other_line in enumerate(text):
        if line == other_line:
            continue
        for let_a, let_b in zip(line, other_line):
            if let_a != let_b:
                not_match_total += 1
        if not_match_total == 1:
            print(line, end='')
            print(other_line, end='')
        else:
            not_match_total = 0

