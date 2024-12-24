import itertools

with open("day23_input.txt") as f:
    lines = f.read().splitlines()
    lines = [e.split("-") for e in lines]


network = {}
edges = set()
for v1, v2 in lines:
    network.setdefault(v1, []).append(v2)
    network.setdefault(v2, []).append(v1)
    edges.add(tuple(sorted((v1, v2))))


candidates = set()
for v1, v2, v3 in itertools.combinations(network.keys(), 3):
    if (
        tuple(sorted((v1, v2))) in edges
        and tuple(sorted((v1, v3))) in edges
        and tuple(sorted((v2, v3))) in edges
        and (v1[0] == "t" or v2[0] == "t" or v3[0] == "t")
    ):
        candidates.add(tuple(sorted((v1, v2, v3))))
print(len(candidates))

candidates = set([(v,) for v in network.keys()])
while True:
    new_candidates = set()
    for c in candidates:
        for n in set(itertools.chain(*[network[v] for v in c])):
            for v in c:
                if tuple(sorted((v, n))) not in edges:
                    break
            else:
                new_candidates.add(tuple(sorted(list(c) + [n])))
    if len(new_candidates) == 0:
        break
    candidates = new_candidates

print(",".join(sorted(list(candidates)[0])))
