from heapq import heappop, heappush

with open("day16_input.txt") as f:
    board = f.read().splitlines()
    board = [list(b) for b in board]
board

for i, line in enumerate(board):
    for j, cell in enumerate(line):
        if cell == "S":
            start = (i, j)
        if cell == "E":
            end = (i, j)


queue = [(0, start, (0, 1))]
scores = {}
scores[(start, (0, 1))] = (0, set([start]))

while len(queue) > 0:
    score, pos, direction = heappop(queue)
    if pos == end:
        break
    if scores.get((pos, direction), (float("inf"), set()))[0] < score:
        continue
    for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if board[pos[0] + d[0]][pos[1] + d[1]] != "#" and (pos[0] + d[0], pos[1] + d[1]):
            score_n, tiles = scores.get(((pos[0] + d[0], pos[1] + d[1]), d), (float("inf"), set()))
            new_score = score + 1 + (1000 if d != direction else 0)
            if new_score < score_n:
                heappush(queue, (new_score, (pos[0] + d[0], pos[1] + d[1]), d))
                new_tiles = set(scores[(pos, direction)][1])
                new_tiles.add((pos[0] + d[0], pos[1] + d[1]))
                scores[((pos[0] + d[0], pos[1] + d[1]), d)] = (new_score, new_tiles)
            if new_score == score_n:
                tiles.update(scores[(pos, direction)][1])


print(min([scores.get((end, d), (float("inf"), set()))[0] for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]]))
print(len(scores[(end, (-1, 0))][1]))
