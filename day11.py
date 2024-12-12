import math

with open("day11_input.txt") as f:
    stones = [int(i) for i in f.read().split()]
blinks = 75
counters = {}
for s in stones:
    counters[s] = counters.get(s, 0) + 1

for b in range(blinks):
    new_counters = {}
    for stone, count in counters.items():
        if stone == 0:
            new_counters[1] = new_counters.get(1, 0) + count
        elif math.floor(math.log10(stone) + 1) % 2 == 0:
            l = math.floor(math.log10(stone) + 1)

            new_counters[int(stone // 10 ** (l / 2))] = new_counters.get(int(stone // 10 ** (l / 2)), 0) + count
            new_counters[int(stone % 10 ** (l / 2))] = new_counters.get(int(stone % 10 ** (l / 2)), 0) + count

        else:
            new_counters[2024 * stone] = new_counters.get(2024 * stone, 0) + count

    counters = new_counters
    if b == 24:
        print(sum(counters.values()))
print(sum(counters.values()))
