with open("day12_input.txt") as f:
    m = f.read().splitlines()
seen = set()
regions = []
for i, line in enumerate(m):
    for j, cell in enumerate(line):
        if (i, j) in seen:
            continue
        seen.add((i, j))
        region = []
        region_type = m[i][j]
        q = [(i, j)]
        while len(q):
            plot = q.pop(0)
            region.append(plot)
            if plot[0] > 0 and m[plot[0] - 1][plot[1]] == region_type and (plot[0] - 1, plot[1]) not in seen:
                seen.add((plot[0] - 1, plot[1]))
                q.append((plot[0] - 1, plot[1]))
            if plot[0] < len(m) - 1 and m[plot[0] + 1][plot[1]] == region_type and (plot[0] + 1, plot[1]) not in seen:
                seen.add((plot[0] + 1, plot[1]))
                q.append((plot[0] + 1, plot[1]))
            if plot[1] > 0 and m[plot[0]][plot[1] - 1] == region_type and (plot[0], plot[1] - 1) not in seen:
                seen.add((plot[0], plot[1] - 1))
                q.append((plot[0], plot[1] - 1))
            if (
                plot[1] < len(m[0]) - 1
                and m[plot[0]][plot[1] + 1] == region_type
                and (plot[0], plot[1] + 1) not in seen
            ):
                seen.add((plot[0], plot[1] + 1))
                q.append((plot[0], plot[1] + 1))
        regions.append(region)
total_price = 0
for region in regions:
    region_type = m[region[0][0]][region[0][1]]
    perimiter = 0
    for plot in region:
        if plot[0] == 0 or m[plot[0] - 1][plot[1]] != region_type:
            perimiter += 1
        if plot[0] == len(m) - 1 or m[plot[0] + 1][plot[1]] != region_type:
            perimiter += 1
        if plot[1] == 0 or m[plot[0]][plot[1] - 1] != region_type:
            perimiter += 1
        if plot[1] == len(m[0]) - 1 or m[plot[0]][plot[1] + 1] != region_type:
            perimiter += 1
    total_price += perimiter * len(region)
print(total_price)

total_price = 0
for region in regions:
    region_type = m[region[0][0]][region[0][1]]
    horizontal_perimiters = {}
    vertical_perimiters = {}
    for plot in region:
        if plot[0] == 0 or m[plot[0] - 1][plot[1]] != region_type:
            horizontal_perimiters[(plot[0], plot[0])] = horizontal_perimiters.get((plot[0], plot[0]), []) + [plot]
        if plot[0] == len(m) - 1 or m[plot[0] + 1][plot[1]] != region_type:
            horizontal_perimiters[(plot[0] + 1, plot[0])] = horizontal_perimiters.get((plot[0] + 1, plot[0]), []) + [
                plot
            ]
        if plot[1] == 0 or m[plot[0]][plot[1] - 1] != region_type:
            vertical_perimiters[(plot[1], plot[1])] = vertical_perimiters.get((plot[1], plot[1]), []) + [plot]
        if plot[1] == len(m[0]) - 1 or m[plot[0]][plot[1] + 1] != region_type:
            vertical_perimiters[(plot[1] + 1, plot[1])] = vertical_perimiters.get((plot[1] + 1, plot[1]), []) + [plot]
    total_side_count = 0
    for h in horizontal_perimiters.values():
        count = 1
        s = sorted([x[1] for x in h])
        for i in range(len(s) - 1):
            if s[i] != s[i + 1] - 1:
                count += 1
        total_side_count += count
    for h in vertical_perimiters.values():
        count = 1
        s = sorted([x[0] for x in h])
        for i in range(len(s) - 1):
            if s[i] != s[i + 1] - 1:
                count += 1
        total_side_count += count
    total_price += total_side_count * len(region)
print(total_price)
