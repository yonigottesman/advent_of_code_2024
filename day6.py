with open("day6_input.txt") as f:
    inputs = [[i for i in l] for l in f.read().splitlines()]
for i, row in enumerate(inputs):
    for j, item in enumerate(row):
        if item == "^":
            start = (i, j)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_index = 0
i, j = start
path = [(i, j, direction_index)]
while i >= 0 and i < len(inputs) and j >= 0 and j < len(inputs[0]):
    next_cell = (i + directions[direction_index][0], j + directions[direction_index][1])
    if next_cell[0] < 0 or next_cell[0] >= len(inputs) or next_cell[1] < 0 or next_cell[1] >= len(inputs[0]):
        break
    if inputs[next_cell[0]][next_cell[1]] == "#":
        direction_index = (direction_index + 1) % 4
    else:
        i += directions[direction_index][0]
        j += directions[direction_index][1]
        path.append((i, j))
print(len(set([(p[0], p[1]) for p in path])))  # 5534


count = 0
distinct_positions = set([(p[0], p[1]) for p in path])
distinct_positions.remove(start)
last_position = start[0], start[1], 0
seen = set()
for d in path:
    if (d[0], d[1]) in seen:
        continue
    seen.add((d[0], d[1]))
    inputs[d[0]][d[1]] = "o"
    pos_dir = set()
    i, j, direction_index = last_position
    while i >= 0 and i < len(inputs) and j >= 0 and j < len(inputs[0]):
        if (i, j, direction_index) in pos_dir:
            count += 1
            break
        pos_dir.add((i, j, direction_index))
        next_cell = (i + directions[direction_index][0], j + directions[direction_index][1])
        if next_cell[0] < 0 or next_cell[0] >= len(inputs) or next_cell[1] < 0 or next_cell[1] >= len(inputs[0]):
            break
        if inputs[next_cell[0]][next_cell[1]] == "#":
            direction_index = (direction_index + 1) % 4
        elif inputs[next_cell[0]][next_cell[1]] == "o":
            last_position = i, j, direction_index
            direction_index = (direction_index + 1) % 4
            inputs[next_cell[0]][next_cell[1]] = "#"
        else:
            i += directions[direction_index][0]
            j += directions[direction_index][1]

    inputs[d[0]][d[1]] = "."
print(count)
