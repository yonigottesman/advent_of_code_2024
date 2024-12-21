with open("day18_input.txt") as f:
    bytes = f.read().splitlines()
bytes = [list(map(int, b.split(","))) for b in bytes]

width = 71


for i in range(1024, len(bytes)):
    # i = len(bytes)
    # print(i)
    memory = []
    for _ in range(width):
        memory.append(["."] * width)

    for X, Y in bytes[:i]:
        memory[Y][X] = "#"

    queue = [((0, 0), 0)]
    seen = set([(0, 0)])
    found_path = False

    while len(queue) > 0:
        pos, dist = queue.pop(0)
        if pos == (70, 70):
            # print(dist)
            found_path = True
            break
        for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if (
                pos[0] + d[0] >= 0
                and pos[1] + d[1] >= 0
                and pos[0] + d[0] < len(memory)
                and pos[1] + d[1] < len(memory[0])
                and memory[pos[0] + d[0]][pos[1] + d[1]] != "#"
                and (pos[0] + d[0], pos[1] + d[1]) not in seen
            ):
                seen.add((pos[0] + d[0], pos[1] + d[1]))
                queue.append(((pos[0] + d[0], pos[1] + d[1]), dist + 1))
    if not found_path:
        print(i)
        break
