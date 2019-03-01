deer = {}
best = 0
MAX_SECONDS = 2503

with open("input14.txt") as file:
    raw_data = [line.strip().split() for line in file.readlines()]


for line in raw_data:
    name = line[0]
    speed = int(line[3])
    speed_time = int(line[6])
    rest_time = int(line[-2])
    deer[name] = {"speed": speed, "speed_time": speed_time, "rest_time": rest_time}

for flyer in deer.values():
    distance = []
    while len(distance) < MAX_SECONDS:
        distance += [flyer["speed"] for _ in range(flyer["speed_time"])]
        distance += [0 for _ in range(flyer["rest_time"])]
    total = sum(distance[:MAX_SECONDS])
    if total > best:
        best = total

print(best)
