with open("day20_input.txt") as f:
    track = f.read().splitlines()

for i, line in enumerate(track):
    for j, cell in enumerate(line):
        if cell == "S":
            start = (i, j)
        elif cell == "E":
            end = (i, j)

path = []
pos = end
dist = {end: 0}
picoseconds = 1
while pos != start:
    path.insert(0, pos)
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if (
            pos[0] + d[0] >= 0
            and pos[0] + d[0] < len(track)
            and pos[1] + d[1] >= 0
            and pos[1] + d[1] < len(track[0])
            and (pos[0] + d[0], pos[1] + d[1]) not in dist
            and track[pos[0] + d[0]][pos[1] + d[1]] != "#"
        ):
            dist[(pos[0] + d[0], pos[1] + d[1])] = picoseconds
            picoseconds += 1
            pos = (pos[0] + d[0], pos[1] + d[1])
            break
path.insert(0, start)

counter = 0
for pos in path:
    for d in [(0, 2), (0, -2), (2, 0), (-2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if (pos[0] + d[0], pos[1] + d[1]) in dist:
            saved = dist[pos] - dist[(pos[0] + d[0], pos[1] + d[1])] - 2
            if saved >= 100:
                counter += 1
print(counter)

ds = []
for j in range(2, 21):
    for i in range(j + 1):
        ds.append((i, j - i))
        ds.append((-i, j - i))
        ds.append((i, -(j - i)))
        ds.append((-i, -(j - i)))

cheats = {}
for pos in path:
    queue = [pos]

    for d in ds:
        if (pos[0] + d[0], pos[1] + d[1]) in dist:
            saved = dist[pos] - dist[(pos[0] + d[0], pos[1] + d[1])] - (abs(d[0]) + abs(d[1]))
            if saved >= 100:
                cheats[(pos, (pos[0] + d[0], pos[1] + d[1]))] = saved
print(len(cheats))
