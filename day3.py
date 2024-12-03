import re


def part1():
    with open("day3_input.txt") as f:
        memory = f.read()
    pattern = r"mul\(([1-9]\d{0,2}),([1-9]\d{0,2})\)"
    matches = re.findall(pattern, memory)
    res = sum([int(m[0]) * int(m[1]) for m in matches])
    print(res)


def part2():
    with open("day3_input.txt") as f:
        memory = f.read()
    matches = list(re.finditer(r"mul\(([1-9]\d{0,2}),([1-9]\d{0,2})\)", memory))
    dodont_matches = list(re.finditer(r"(do\(\))|(don't\(\))", memory))
    matches.extend(dodont_matches)
    on = True
    res = 0
    for m in sorted(matches, key=lambda x: x.span()[0]):
        if on and m.group().startswith("mul"):
            res += int(m.group(1)) * int(m.group(2))
        elif m.group() == "do()":
            on = True
        else:
            on = False
    print(res)


if __name__ == "__main__":
    part1()
    part2()
