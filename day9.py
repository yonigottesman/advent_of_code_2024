with open("day9_input.txt") as f:
    diskmap = f.read()


memory = []
idnum = 0
free_indices = []
for i, block_size in enumerate(diskmap):
    if i % 2 == 0:
        memory.extend([idnum] * int(block_size))
        idnum += 1
    else:
        free_indices.extend(
            range(
                len(memory),
                len(
                    memory,
                )
                + int(block_size),
            )
        )
        memory.extend(["."] * int(block_size))
i = -1
while free_indices:
    if memory[i] == ".":
        i -= 1
        continue
    free_space = free_indices.pop(0)
    if free_space > len(memory) + i:
        continue
    memory[free_space] = memory[i]
    memory[i] = "."
    i -= 1
checksum = 0
for i, m in enumerate(memory):
    if m == ".":
        break
    checksum += i * m
print(checksum)

# part 2
memory = []
idnum = 0
free_indices = []
blocks = []
for i, block_size in enumerate(diskmap):
    if i % 2 == 0:
        blocks.append((idnum, len(memory), int(block_size)))
        memory.extend([idnum] * int(block_size))
        idnum += 1
    else:
        free_indices.append((len(memory), int(block_size)))
        memory.extend(["."] * int(block_size))


i = -1
while len(blocks) + i >= 0:
    b = blocks[i]
    j = 0
    while b[1] > free_indices[j][0]:
        f = free_indices[j]
        if b[2] <= f[1]:
            for x in range(b[2]):
                memory[f[0] + x] = b[0]
                memory[b[1] + x] = "."
            if b[2] == f[1]:
                free_indices.pop(j)
            else:
                free_indices[j] = (free_indices[j][0] + b[2], free_indices[j][1] - b[2])
            break
        else:
            j += 1

    i -= 1

checksum = 0
for i, m in enumerate(memory):
    if m == ".":
        continue
    checksum += i * m
print(checksum)
