import json


def unpack(spam, total=0, trigger=False):

    if trigger:
        return total

    if isinstance(spam, list):
        for thing in spam:
            if isinstance(thing, (list, dict)):
                total += unpack(thing)
            elif isinstance(thing, int):
                total += thing

    elif isinstance(spam, dict):
        if "red" in spam.values():
            trigger = True
        for key, value in spam.items():
            if isinstance(value, (list, dict)):
                total += unpack(value, trigger=trigger)
            elif isinstance(value, int) and not trigger:
                total += value

    return total


with open("input12.json") as file:
    data = json.load(file)

grand_total = unpack(data)
print(grand_total)
