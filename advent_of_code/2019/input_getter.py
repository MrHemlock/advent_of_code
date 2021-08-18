import os
import requests


def get_input(day: int) -> None:
    input_url = f"https://adventofcode.com/2019/day/{day}/input"

    if not os.path.exists(f"inputs/day_{day}_input.txt"):
        print("Input file not found, retrieving from Advent site.")
        cookies = {"session": os.environ.get("AOC_SESSION")}
        response = requests.get(input_url, cookies=cookies)
        if response.status_code.ok:
            with open(f"inputs/day_{day}_input.txt", "w") as file:
                file.write(response.text)
        else:
            print("Something went wrong")
