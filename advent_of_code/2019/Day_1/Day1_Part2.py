def _fuel_process(fuel):
    processed = (fuel // 3) - 2
    if processed > 0:
        return processed + _fuel_process(processed)
    return 0


def main():
    with open("inputs/day_1_input.txt") as file:
        data = [int(line) for line in file]

    total = sum(map(_fuel_process, data))
    print(total)


if __name__ == "__main__":
    main()
