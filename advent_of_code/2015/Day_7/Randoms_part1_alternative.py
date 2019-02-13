assert(line[-2] == '->')
var = line[-1]
expr = line[:-2]

def get_value(value):
    try:
        return int(value)
    except ValueError:
        return wires[value]  # if KeyError what

if len(expr) == 1:
    value = get_value(expr[0])
    wires[var] = value
elif len(expr) == 2:
    op, value = expr
    value = get_value(value)
    ...
elif len(expr) == 3:
    value1, op, value2 = expr
    value1 = get_value(value1)
    value2 = get_value(value2)
    ...