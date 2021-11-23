from collections import Counter

#  Ending value is 1 higher for ease of use in range
PROBLEM_RANGE = (234208, 765870)


def main():
    total = 0
    for num in range(*PROBLEM_RANGE):
        str_num = str(num)
        if ''.join(sorted(str_num)) == str_num:
            if 2 in Counter(str_num).values():
                total += 1
    print(total)


if __name__ == "__main__":
    main()
