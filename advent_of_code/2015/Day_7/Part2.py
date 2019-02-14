data = []
clean_data = []
wires = dict()
validated = set()


def get_value(value, wire_dict):
    try:
        return int(value)
    except ValueError:
        if value in wire_dict:
            return wire_dict[value]
        else:
            raise KeyError


def bit_not(value, mask=0xFFFF):
    return value ^ mask


def bit_and(x, y, mask=0xFFFF):
    return (x & y) & mask


def bit_or(x, y, mask=0xFFFF):
    return (x | y) & mask


def bit_lshift(x, y, mask=0xFFFF):
    return (x << y) & mask


def bit_rshift(x, y, mask=0xFFFF):
    return (x >> y) & mask


bit_dict = {"AND": bit_and, "OR": bit_or, "LSHIFT": bit_lshift, "RSHIFT": bit_rshift}


with open('input7_2.txt') as file:
    data = [tuple(line.split()) for line in file]


while len(validated) < len(data):
    for line in data:
        var = line[-1]
        expr = line[:-2]
        if line in validated:
            continue

        try:
            if len(expr) == 1:
                wires[var] = get_value(expr[0], wires)

            elif len(expr) == 2:
                wires[var] = bit_not(get_value(expr[1], wires))

            elif len(expr) == 3:
                x = get_value(expr[0], wires)
                y = get_value(expr[2], wires)
                wires[var] = bit_dict[expr[1]](x, y)

            validated.add(line)

        except KeyError:
            continue

print(wires['a'])
print(wires['b'])
