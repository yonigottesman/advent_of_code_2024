numeric_map = {
    "0": (3, 1),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "A": (3, 2),
}
directional_map = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}
res = 0
for code in ["803A", "528A", "586A", "341A", "319A"]:
    pos = numeric_map["A"]
    seqs = [[]]
    for c in code:
        dest = numeric_map[c]
        horizon = pos[1] - dest[1]
        vert = pos[0] - dest[0]

        if horizon != 0 and vert != 0:
            if pos in [(3, 1), (3, 2)] and dest in [(0, 0), (1, 0), (2, 0)]:
                [seq.extend(["^" if vert > 0 else "v"] * abs(vert)) for seq in seqs]
                [seq.extend(["<" if horizon > 0 else ">"] * abs(horizon) + ["A"]) for seq in seqs]
            elif dest in [(3, 1), (3, 2)] and pos in [(0, 0), (1, 0), (2, 0)]:
                [seq.extend(["<" if horizon > 0 else ">"] * abs(horizon)) for seq in seqs]
                [seq.extend(["^" if vert > 0 else "v"] * abs(vert) + ["A"]) for seq in seqs]
            else:
                split_a = [s.copy() for s in seqs]
                for s in split_a:
                    s.extend(["^" if vert > 0 else "v"] * abs(vert))
                    s.extend(["<" if horizon > 0 else ">"] * abs(horizon))
                    s.append("A")
                split_b = [s.copy() for s in seqs]
                for s in split_b:
                    s.extend(["<" if horizon > 0 else ">"] * abs(horizon))
                    s.extend(["^" if vert > 0 else "v"] * abs(vert))
                    s.append("A")
                seqs = split_a + split_b
        else:
            [seq.extend(["^" if vert > 0 else "v"] * abs(vert)) for seq in seqs]
            [seq.extend(["<" if horizon > 0 else ">"] * abs(horizon) + ["A"]) for seq in seqs]
        pos = dest

    min_len = float("inf")
    for s in seqs:
        seq = s
        for _ in range(2):
            pcode = "".join(seq)
            pos = directional_map["A"]
            seq = []
            for c in pcode:
                dest = directional_map[c]
                horizon = pos[1] - dest[1]
                vert = pos[0] - dest[0]
                if pos == (1, 0):
                    seq.extend(["<" if horizon > 0 else ">"] * abs(horizon))
                    seq.extend(["^" if vert > 0 else "v"] * abs(vert))
                else:
                    seq.extend(["^" if vert > 0 else "v"] * abs(vert))
                    seq.extend(["<" if horizon > 0 else ">"] * abs(horizon))

                seq.append("A")
                pos = dest
        pcode = "".join(seq)
        min_len = min(min_len, len(pcode))
    res += min_len * int(code[:-1])
print(res)


# res = 0
# # for code in ["803A", "528A", "586A", "341A", "319A"]:
# code = "803A"
# pos = numeric_map["A"]
# seqs = [[]]
# for c in code:
#     dest = numeric_map[c]
#     horizon = pos[1] - dest[1]
#     vert = pos[0] - dest[0]

#     if horizon != 0 and vert != 0:
#         if pos in [(3, 1), (3, 2)] and dest in [(0, 0), (1, 0), (2, 0)]:
#             [seq.extend(["^" if vert > 0 else "v"] * abs(vert)) for seq in seqs]
#             [seq.extend(["<" if horizon > 0 else ">"] * abs(horizon) + ["A"]) for seq in seqs]
#         elif dest in [(3, 1), (3, 2)] and pos in [(0, 0), (1, 0), (2, 0)]:
#             [seq.extend(["<" if horizon > 0 else ">"] * abs(horizon)) for seq in seqs]
#             [seq.extend(["^" if vert > 0 else "v"] * abs(vert) + ["A"]) for seq in seqs]
#         else:
#             split_a = [s.copy() for s in seqs]
#             for s in split_a:
#                 s.extend(["^" if vert > 0 else "v"] * abs(vert))
#                 s.extend(["<" if horizon > 0 else ">"] * abs(horizon))
#                 s.append("A")
#             split_b = [s.copy() for s in seqs]
#             for s in split_b:
#                 s.extend(["<" if horizon > 0 else ">"] * abs(horizon))
#                 s.extend(["^" if vert > 0 else "v"] * abs(vert))
#                 s.append("A")
#             seqs = split_a + split_b
#     else:
#         [seq.extend(["^" if vert > 0 else "v"] * abs(vert)) for seq in seqs]
#         [seq.extend(["<" if horizon > 0 else ">"] * abs(horizon) + ["A"]) for seq in seqs]
#     pos = dest

# for i in range(25):
#     print(i)
#     new_seqs = []
#     for s in seqs:
#         pcode = "".join(s)
#         pos = directional_map["A"]
#         current_seqs = [[]]
#         for c in pcode:
#             dest = directional_map[c]
#             horizon = pos[1] - dest[1]
#             vert = pos[0] - dest[0]
#             if horizon != 0 and vert != 0:
#                 if pos == (0, 1) and dest == (1, 0):
#                     [seq.extend(["^" if vert > 0 else "v"] * abs(vert)) for seq in current_seqs]
#                     [seq.extend(["<" if horizon > 0 else ">"] * abs(horizon) + ["A"]) for seq in current_seqs]
#                 elif pos == (1, 0) and dest == (0, 1):
#                     [seq.extend(["<" if horizon > 0 else ">"] * abs(horizon) + ["A"]) for seq in current_seqs]
#                     [seq.extend(["^" if vert > 0 else "v"] * abs(vert)) for seq in current_seqs]
#                 else:
#                     split_a = [s.copy() for s in current_seqs]
#                     for s in split_a:
#                         s.extend(["^" if vert > 0 else "v"] * abs(vert))
#                         s.extend(["<" if horizon > 0 else ">"] * abs(horizon))
#                         s.append("A")
#                     split_b = [s.copy() for s in current_seqs]
#                     for s in split_b:
#                         s.extend(["<" if horizon > 0 else ">"] * abs(horizon))
#                         s.extend(["^" if vert > 0 else "v"] * abs(vert))
#                         s.append("A")
#                     current_seqs = split_a + split_b
#             else:
#                 [seq.extend(["^" if vert > 0 else "v"] * abs(vert)) for seq in current_seqs]
#                 [seq.extend(["<" if horizon > 0 else ">"] * abs(horizon) + ["A"]) for seq in current_seqs]

#             pos = dest
#         new_seqs.extend(current_seqs)
#     seqs = new_seqs
# min(map(len, seqs))
