with open("Day_2_input.txt") as file:
    data: list[str] = [line.strip() for line in file.readlines()]

position: int = 5
combo: list[int] = []

for line in data:
    for char in line:
        match char:
            case 'U' if position not in (1, 2, 3):
                position -= 3
            case 'D' if position not in (7, 8, 9):
                position += 3
            case 'L' if position not in (1, 4, 7):
                position -= 1
            case 'R' if position not in (3, 6, 9):
                position += 1

    combo.append(position)

print(*combo)
