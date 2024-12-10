with open("day10_input.txt") as f:
    m = [[int(i) for i in line] for line in f.read().splitlines()]

global_count = 0
for i, line in enumerate(m):
    for j, cell in enumerate(line):
        if cell == 0:
            q = [(i, j)]
            count = 0
            seen = set([i, j])
            while len(q):
                current = q.pop(0)
                current_value = m[current[0]][current[1]]
                if m[current[0]][current[1]] == 9:
                    count += 1
                if (
                    current[1] > 0
                    and m[current[0]][current[1] - 1] == current_value + 1
                    and (current[0], current[1] - 1) not in seen
                ):
                    seen.add((current[0], current[1] - 1))
                    q.append((current[0], current[1] - 1))
                if (
                    current[1] < len(m[0]) - 1
                    and m[current[0]][current[1] + 1] == current_value + 1
                    and (current[0], current[1] + 1) not in seen
                ):
                    seen.add((current[0], current[1] + 1))
                    q.append((current[0], current[1] + 1))
                if (
                    current[0] > 0
                    and m[current[0] - 1][current[1]] == current_value + 1
                    and (current[0] - 1, current[1]) not in seen
                ):
                    seen.add((current[0] - 1, current[1]))
                    q.append((current[0] - 1, current[1]))
                if (
                    current[0] < len(m) - 1
                    and m[current[0] + 1][current[1]] == current_value + 1
                    and (current[0] + 1, current[1]) not in seen
                ):
                    seen.add((current[0] + 1, current[1]))
                    q.append((current[0] + 1, current[1]))
            global_count += count
print(global_count)

global_count = 0
for i, line in enumerate(m):
    for j, cell in enumerate(line):
        if cell == 0:
            q = [(i, j)]
            count = 0
            while len(q):
                current = q.pop(0)
                current_value = m[current[0]][current[1]]
                if m[current[0]][current[1]] == 9:
                    count += 1
                if current[1] > 0 and m[current[0]][current[1] - 1] == current_value + 1:
                    q.append((current[0], current[1] - 1))
                if current[1] < len(m[0]) - 1 and m[current[0]][current[1] + 1] == current_value + 1:
                    q.append((current[0], current[1] + 1))
                if current[0] > 0 and m[current[0] - 1][current[1]] == current_value + 1:
                    q.append((current[0] - 1, current[1]))
                if current[0] < len(m) - 1 and m[current[0] + 1][current[1]] == current_value + 1:
                    q.append((current[0] + 1, current[1]))
            global_count += count
print(global_count)
