previous_num = None


with open("input10.txt") as file:
    data = file.read().strip()

for _ in range(50):
    new_string = ""
    for index, num in enumerate(data):
        total = 1
        temp_index = index
        flag = False
        while True:
            try:
                if previous_num is None or previous_num != num:
                    if num == data[temp_index+1]:
                        temp_index += 1
                        total += 1
                    else:
                        break
                else:
                    flag = True
                    break
            except IndexError:
                break
        previous_num = num
        if not flag:
            new_string += str(total) + num
    data = new_string
    previous_num = None


print(len(data))
