from math import sqrt

house_num = 33100000
lowest_house = house_num


def factor(n: int) -> set:

    elves = {1, n}

    elves.update(i for i in range(1, int(sqrt(n)) + 1) if n % i == 0)

    return elves


baseline = sum(factor(house_num)) * 10
print(baseline)

for i in range(1, house_num):
    presents = sum(factor(i)) * 10
    print(i)

    if lowest_house > i and presents >= baseline:
        print(presents)
        lowest_house = i
        print(f"New lowest house: {lowest_house}")
        break


print(lowest_house)
