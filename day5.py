def part1():
    with open("day5_input.txt") as f:
        inputs = f.read().splitlines()
    s = inputs.index("")
    updates = [tuple(map(int, u.split(","))) for u in inputs[s + 1 :]]
    rules = [tuple(map(int, r.split("|"))) for r in inputs[:s]]
    result = 0
    for u in updates:
        relevant_rules = [r for r in rules if r[0] in u and r[1] in u]
        befores_map = {r[1]: [] for r in relevant_rules}
        for r in relevant_rules:
            befores_map[r[1]].append(r[0])
        valid = set(u)
        for i in u:
            if i not in valid:
                break
            valid = valid.difference(befores_map.get(i, []))
        else:
            result += u[int(len(u) / 2)]
    print(result)  # 5208


def part2():
    with open("day5_input.txt") as f:
        inputs = f.read().splitlines()
    s = inputs.index("")
    updates = [tuple(map(int, u.split(","))) for u in inputs[s + 1 :]]
    rules = [tuple(map(int, r.split("|"))) for r in inputs[:s]]

    incorrectly = []
    for u in updates:
        relevant_rules = [r for r in rules if r[0] in u and r[1] in u]
        befores_map = {r[1]: [] for r in relevant_rules}
        for r in relevant_rules:
            befores_map[r[1]].append(r[0])
        valid = set(u)
        for i in u:
            if i not in valid:
                incorrectly.append(u)
                break
            valid = valid.difference(befores_map.get(i, []))

    result = 0
    for u in incorrectly:
        relevant_rules = [r for r in rules if r[0] in u and r[1] in u]
        befores_map = {}
        afters_map = {r[0]: set() for r in relevant_rules}
        roots = set(u)
        for r in relevant_rules:
            befores_map[r[1]] = befores_map.get(r[1], 0) + 1
            if r[1] in roots:
                roots.remove(r[1])
            afters_map[r[0]].add(r[1])
        new_order = []
        while len(roots) > 0:
            current = roots.pop()
            new_order.append(current)
            for i in afters_map.get(current, []):
                befores_map[i] = befores_map[i] - 1
                if befores_map[i] == 0:
                    roots.add(i)
        result += new_order[int(len(new_order) / 2)]
    print(result)  # 6732


if __name__ == "__main__":
    part1()
    part2()
