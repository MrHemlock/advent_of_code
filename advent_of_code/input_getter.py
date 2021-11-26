import os
from pathlib import Path

from dotenv import load_dotenv
import requests

load_dotenv()

def get_input() -> None:
    year = int(input("Which year?  "))
    day = int(input("Which day?  "))
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    input_path = Path(f"{year}/Day_{day}/Day_{day}_input.txt")

    if not input_path.exists():
        print("Input file not found, retrieving from Advent site.")
        cookies = {"session": os.environ.get("AOC_SESSION")}
        response = requests.get(input_url, cookies=cookies)
        if response.ok:
            with open(input_path, "w") as file:
                file.write(response.text)
        else:
            print("Something went wrong")
            print(response)
    else:
        print("Input file found. Not downloading.")


if __name__ == "__main__":
    get_input()
