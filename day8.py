with open("day8_input.txt") as f:
    lines = f.read().splitlines()

freqs = {}
for i, line in enumerate(lines):
    for j, cell in enumerate(line):
        if cell == ".":
            continue
        freqs[cell] = freqs.get(cell, []) + [(i, j)]
antinodes = set()
for freq in freqs.values():
    for i, f1 in enumerate(freq):
        for f2 in freq[i + 1 :]:
            row_diff = f1[0] - f2[0]
            col_diff = f1[1] - f2[1]
            antinode1 = (f1[0] + row_diff, f1[1] + col_diff)
            antinode2 = (f2[0] - row_diff, f2[1] - col_diff)
            if antinode1[0] >= 0 and antinode1[0] < len(lines) and antinode1[1] >= 0 and antinode1[1] < len(lines[0]):
                antinodes.add(antinode1)
            if antinode2[0] >= 0 and antinode2[0] < len(lines) and antinode2[1] >= 0 and antinode2[1] < len(lines[0]):
                antinodes.add(antinode2)
print(len(antinodes))


antinodes = set()
# freq = freqs["0"]
for freq in freqs.values():
    for i, f1 in enumerate(freq):
        for f2 in freq[i + 1 :]:
            row_diff = f1[0] - f2[0]
            col_diff = f1[1] - f2[1]
            antinode1 = f1
            antinode2 = f2
            while (
                antinode1[0] >= 0 and antinode1[0] < len(lines) and antinode1[1] >= 0 and antinode1[1] < len(lines[0])
            ):
                antinodes.add(antinode1)
                antinode1 = (antinode1[0] + row_diff, antinode1[1] + col_diff)
            while (
                antinode2[0] >= 0 and antinode2[0] < len(lines) and antinode2[1] >= 0 and antinode2[1] < len(lines[0])
            ):
                antinodes.add(antinode2)
                antinode2 = (antinode2[0] - row_diff, antinode2[1] - col_diff)
print(len(antinodes))
