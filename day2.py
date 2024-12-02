def safe(report):
    reports = [s - t for s, t in zip(report, report[1:])]
    for d in reports:
        if abs(d) < 1 or abs(d) > 3 or d * reports[0] < 0:
            return False
    return True


def part2():
    with open("day2_input.txt") as f:
        reports = f.read().splitlines()
    reports = (list(map(int, r.split(" "))) for r in reports)
    count = 0
    for r in reports:
        if safe(r):
            count += 1
        else:
            for i in range(len(r)):
                new_r = r[0:i] + r[i + 1 :]
                if safe(new_r):
                    count += 1
                    break
    print(count)  # 439


def part1():
    with open("day2_input.txt") as f:
        reports = f.read().splitlines()
    reports = (list(map(int, r.split(" "))) for r in reports)
    count = 0
    for r in reports:
        if safe(r):
            count += 1
    print(count)  # 390


if __name__ == "__main__":
    part1()
    part2()
