def part1():
    with open("day1_input.txt") as f:
        lines = f.read()
    a, b = zip(*(l.split() for l in lines.split("\n") if l))
    a = sorted(map(int, a))
    b = sorted(map(int, b))
    result = sum(map(lambda x, y: abs(x - y), a, b))
    print(result)  # 2344935


def part2():
    with open("day1_input.txt") as f:
        lines = f.read()
    a, b = zip(*(l.split() for l in lines.split("\n") if l))
    a = map(int, a)
    b = list(map(int, b))
    result = 0
    for i in a:
        result += b.count(i) * i
    print(result)  # 27647262


if __name__ == "__main__":
    part1()
    part2()
