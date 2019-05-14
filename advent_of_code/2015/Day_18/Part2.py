total = 0


def light_logic(lights):
    new_lights = []
    for i, row in enumerate(lights):
        new_lights.append([])
        for j, light in enumerate(row):
            if i in (0, 99) and j in (0, 99):
                new_lights[i].append("#")
                continue
            if i == 0:
                if j == 0:
                    group = [lights[i][j + 1]] + lights[i + 1][j:j + 2]
                elif j == (len(row) - 1):
                    group = [lights[i][j - 1]] + lights[i + 1][j - 1:j + 1]
                else:
                    group = lights[i][j - 1:j + 2:2] + lights[i + 1][j - 1:j + 2]
            elif i == (len(lights) - 1):
                if j == 0:
                    group = lights[i - 1][j:j + 2] + [lights[i][j + 1]]
                elif j == (len(row) - 1):
                    group = lights[i - 1][j - 1:j + 1] + [lights[i][j - 1]]
                else:
                    group = lights[i - 1][j - 1:j + 2] + lights[i][j - 1:j + 2:2]
            else:
                if j == 0:
                    group = lights[i - 1][j:j + 2] + [lights[i][j + 1]] + lights[i + 1][j:j + 2]
                elif j == (len(row) - 1):
                    group = lights[i - 1][j - 1:j + 1] + [lights[i][j - 1]] + lights[i + 1][j - 1:j + 1]
                else:
                    group = lights[i-1][j - 1:j + 2] + lights[i][j - 1:j + 2:2] + lights[i + 1][j - 1:j + 2]

            if light == "#":
                if group.count("#") in (2, 3):
                    new_lights[i].append("#")
                else:
                    new_lights[i].append(".")
            else:
                if group.count("#") == 3:
                    new_lights[i].append("#")
                else:
                    new_lights[i].append(".")
    return new_lights


with open("input18.txt") as file:
    light_grid = [[let for let in line.strip()] for line in file]
print(light_grid)

for _ in range(100):
    light_grid = light_logic(light_grid)
    # print(light_grid)

light_grid[0][0], light_grid[0][99], light_grid[99][0], light_grid[99][99] = "#" * 4

for row in light_grid:
    for char in row:
        if char == "#":
            total += 1
print(total)
