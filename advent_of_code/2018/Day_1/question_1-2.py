total = 0
freqs = set()
flag = False
nums = None

with open('input1.txt') as file:
    nums = list(file)
    print(nums)

while True:
    for num in nums:
        total += int(num)
        if total in freqs:
            print(total)
            flag = True
            break
        else:
            freqs.add(total)
    if flag:
        break
