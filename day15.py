with open("day15_input.txt") as f:
    board, moves = f.read().split("\n\n")
board = board.splitlines()
board = [list(l) for l in board]

pos = None
for i, line in enumerate(board):
    for j, cell in enumerate(line):
        if cell == "@":
            pos = (i, j)
stepmap = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
for m in moves:
    if m == "\n":
        continue
    run = pos
    step = stepmap[m]
    while board[run[0]][run[1]] != "#" and board[run[0]][run[1]] != ".":
        run = run[0] + step[0], run[1] + step[1]
    if board[run[0]][run[1]] == "#":
        # found wall before free space do nothing
        pass
    else:
        board[pos[0] + step[0]][pos[1] + step[1]] = "@"
        board[pos[0]][pos[1]] = "."
        if (pos[0] + step[0], pos[1] + step[1]) != run:
            board[run[0]][run[1]] = "O"
        pos = (pos[0] + step[0], pos[1] + step[1])
agg = 0
for i, line in enumerate(board):
    for j, cell in enumerate(line):
        if cell == "O":
            agg += 100 * i + j
print(agg)


with open("day15_input.txt") as f:
    board, moves = f.read().split("\n\n")
board = board.splitlines()
board = [list(l) for l in board]
new_board = []
for line in board:
    newline = []
    for cell in line:
        if cell == "#":
            newline.extend(["#", "#"])
        elif cell == "O":
            newline.extend(["[", "]"])
        elif cell == ".":
            newline.extend([".", "."])
        elif cell == "@":
            newline.extend(["@", "."])
    new_board.append(newline)
board = new_board

pos = None
for i, line in enumerate(board):
    for j, cell in enumerate(line):
        if cell == "@":
            pos = (i, j)


stepmap = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
for m in moves:
    if m == "\n":
        continue
    run = pos
    step = stepmap[m]
    if m == "<" or m == ">":
        while board[run[0]][run[1]] != "#" and board[run[0]][run[1]] != ".":
            run = run[0] + step[0], run[1] + step[1]
        if board[run[0]][run[1]] == "#":
            # found wall before free space do nothing
            pass
        elif (pos[0] + step[0], pos[1] + step[1]) == run:
            board[pos[0]][pos[1]] = "."
            board[pos[0] + step[0]][pos[1] + step[1]] = "@"
            pos = (pos[0] + step[0], pos[1] + step[1])

        else:
            while (run[0], run[1] - step[1]) != pos:
                board[run[0]][run[1]] = board[run[0]][run[1] - step[1]]
                board[run[0]][run[1] - step[1]] = board[run[0]][run[1] - 2 * step[1]]
                run = run[0], run[1] - 2 * step[1]
            board[pos[0] + step[0]][pos[1] + step[1]] = "@"
            board[pos[0]][pos[1]] = "."
            pos = (pos[0] + step[0], pos[1] + step[1])
    else:
        q = []
        seen = set()
        if board[pos[0] + step[0]][pos[1]] == "[":
            q.append((pos[0] + step[0], pos[1]))
            seen.add((pos[0] + step[0], pos[1]))
        elif board[pos[0] + step[0]][pos[1]] == "]":
            q.append((pos[0] + step[0], pos[1] - 1))
            seen.add((pos[0] + step[0], pos[1] - 1))
        while len(q) > 0:
            current = q.pop(0)
            if board[current[0] + step[0]][current[1]] == "#" or board[current[0] + step[0]][current[1] + 1] == "#":
                seen = set()
                break
            if board[current[0] + step[0]][current[1]] == "[":
                seen.add((current[0] + step[0], current[1]))
                q.append((current[0] + step[0], current[1]))
            if board[current[0] + step[0]][current[1] + 1] == "[":
                seen.add((current[0] + step[0], current[1] + 1))
                q.append((current[0] + step[0], current[1] + 1))
            if board[current[0] + step[0]][current[1]] == "]":
                seen.add((current[0] + step[0], current[1] - 1))
                q.append((current[0] + step[0], current[1] - 1))
        for p in seen:
            board[p[0]][p[1]] = "."
            board[p[0]][p[1] + 1] = "."

        for p in seen:
            board[p[0] + step[0]][p[1]] = "["
            board[p[0] + step[0]][p[1] + 1] = "]"
        if len(seen) > 0 or board[pos[0] + step[0]][pos[1] + step[1]] == ".":
            board[pos[0] + step[0]][pos[1] + step[1]] = "@"
            board[pos[0]][pos[1]] = "."
            pos = (pos[0] + step[0], pos[1] + step[1])


agg = 0
for i, line in enumerate(board):
    for j, cell in enumerate(line):
        if cell == "[":
            # agg += 100 * min(i, len(board) - i - 1) + min(j, len(line) - j - 2)
            agg += 100 * i + j
print(agg)
