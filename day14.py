import re

with open("day14_input.txt") as f:
    robots_lines = f.read().splitlines()
seconds = 100
width = 101
hight = 103
quadrants = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
for r in robots_lines:
    px, py, vx, vy = map(int, re.search(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)", r).groups())
    pos = (px + vx * seconds) % width, (py + vy * seconds) % hight
    if pos[0] == (width - 1) / 2 or pos[1] == (hight - 1) / 2:
        continue
    q = 0 if pos[0] < (width - 1) / 2 else 1, 0 if pos[1] < (hight - 1) / 2 else 1
    quadrants[q] = quadrants[q] + 1
print(quadrants[0, 0] * quadrants[1, 0] * quadrants[0, 1] * quadrants[1, 1])


with open("day14_input.txt") as f:
    robots_lines = f.read().splitlines()


def tree_depth(pos, floor):
    depth = 1
    while True:
        for i in range(depth):
            if pos[1] + depth == len(floor) or pos[0] + i == len(floor[0]) or pos[0] - i < 0:
                return depth - 1
            if floor[pos[1] + depth - 1][pos[0] + i] == 0:
                return depth - 1
            if floor[pos[1] + depth - 1][pos[0] - i] == 0:
                return depth - 1
        depth += 1


seconds = 100
width = 101
hight = 103

floor = []
for i in range(hight):
    l = []
    for j in range(width):
        l.append(0)
    floor.append(l)
robots = []
for r in robots_lines:
    px, py, vx, vy = map(int, re.search(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)", r).groups())
    pos = px, py
    floor[pos[1]][pos[0]] = floor[pos[1]][pos[0]] + 1
    robots.append((pos, (vx, vy)))
seconds = 0
while True:
    for r in robots:
        if tree_depth(r[0], floor) > 10:  # WTF THIS IS SO RANDOM!?!@@#$
            print(seconds)
            exit(0)
    new_robots = []
    for r in robots:
        pos, (vx, vy) = r
        new_pos = (pos[0] + vx * 1) % width, (pos[1] + vy * 1) % hight
        floor[pos[1]][pos[0]] = floor[pos[1]][pos[0]] - 1
        floor[new_pos[1]][new_pos[0]] = floor[new_pos[1]][new_pos[0]] + 1
        new_robots.append((new_pos, (vx, vy)))
    robots = new_robots
    seconds += 1
