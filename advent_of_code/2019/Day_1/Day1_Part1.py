import os
import requests

INPUT_URL = "https://adventofcode.com/2019/day/1/input"


if not os.path.exists("inputs/day_1_input.txt"):
    print("Input file not found, retrieving from Advent site.")
    cookies = {"session": os.environ.get("AOC_SESSION")}
    response = requests.get(INPUT_URL, cookies=cookies)
    with open("inputs/day_1_input.txt", "w") as file:
        file.write(response.text)

with open("inputs/day_1_input.txt") as file:
    data = [int(line) for line in file]


total = sum([(mass // 3) - 2 for mass in data])
print(total)
