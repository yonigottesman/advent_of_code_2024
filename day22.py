with open("day22_input.txt") as f:
    secret_numbers = map(int, f.read().splitlines())
generated = []
for secret_number in secret_numbers:
    for _ in range(2000):
        secret_number = ((64 * secret_number) ^ (secret_number)) % 16777216
        secret_number = (int(secret_number / 32) ^ secret_number) % 16777216
        secret_number = ((secret_number * 2048) ^ secret_number) % 16777216
    generated.append(secret_number)
print(sum(generated))


from itertools import chain

with open("day22_input.txt") as f:
    secret_numbers = list(map(int, f.read().splitlines()))

all_seqs = {}
for s in secret_numbers:
    secret_number = s
    generated = [secret_number]
    for _ in range(2000):
        secret_number = ((64 * secret_number) ^ (secret_number)) % 16777216
        secret_number = (int(secret_number / 32) ^ secret_number) % 16777216
        secret_number = ((secret_number * 2048) ^ secret_number) % 16777216
        generated.append(secret_number)
    prices = [g % 10 for g in generated]
    changes = [(j - i, j) for i, j in zip(prices, prices[1:])]

    seqs = {}
    for i, (c, p) in enumerate(changes[3:], 3):
        seq = tuple([c[0] for c in changes[i - 3 : i + 1]])
        if seq not in seqs:
            seqs[seq] = p
    all_seqs[s] = seqs
checked = {}
max_bananas = float("-inf")

for i, seq in enumerate(set(chain(*[[k for k, v in all_seqs[i].items()] for i in all_seqs.keys()]))):
    bananas = 0
    for _, v in all_seqs.items():
        bananas += v.get(seq, 0)
    max_bananas = max(max_bananas, bananas)
print(max_bananas)
