with open("Day_2_input.txt") as file:
    data: list[str] = [line.strip() for line in file.readlines()]

position: int = 5
combo: list[int] = []
converter: dict[int, str] = {10: "A", 11: "B", 12: "C", 13: "D"}

for line in data:
    for char in line:
        match char:
            case 'U' if position in (3, 13):
                position -= 2
            case 'U' if position in (6, 7, 8, 10, 11, 12):
                position -= 4
            case 'D' if position in (1, 11):
                position += 2
            case 'D' if position in (2, 3, 4, 6, 7, 8):
                position += 4
            case 'L' if position not in (1, 2, 5, 10, 13):
                position -= 1
            case 'R' if position not in (1, 4, 9, 12, 13):
                position += 1

    combo.append(position)

print(*[converter.get(num, num) for num in combo])
