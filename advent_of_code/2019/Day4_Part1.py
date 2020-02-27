#  Ending value is 1 higher for ease of use in range
PROBLEM_RANGE = (234208, 765870)


def main():
    total = 0
    for num in range(*PROBLEM_RANGE):
        str_num = str(num)

        if (
                # Checks to see if there are any matching pairs
                any(str_num[i] == str_num[i + 1] for i in range(5)) and
                # Checks to make sure numbers never decrease
                all(str_num[i] <= str_num[i + 1] for i in range(5))
        ):
            total += 1
    print(total)


if __name__ == "__main__":
    main()
