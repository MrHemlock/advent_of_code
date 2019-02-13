data = []
clean_data = []
wires = dict()

def get_value(value):
    pass



with open('input7.txt') as file:
    data = [line.split() for line in file]

for line in data:
    var = line[-1]
    expr = line[:-2]

    if len(expr) == 1:
        try:
            wires[var] = int(expr[0])
        except ValueError:
            try:
                wires[line[2]] = wires[line[0]]
            except KeyError:
                continue

    elif len(line) == 4:
        pass



print(wires['a'])
