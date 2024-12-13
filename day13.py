import re
from fractions import Fraction

with open("day13_input.txt") as f:
    machines = f.read()

total = 0
for m in machines.split("\n\n"):
    Ax, Ay = map(int, re.search(r"X\+(\d+), Y\+(\d+)", m.splitlines()[0]).groups())
    Bx, By = map(int, re.search(r"X\+(\d+), Y\+(\d+)", m.splitlines()[1]).groups())
    Px, Py = map(int, re.search(r"X\=(\d+), Y\=(\d+)", m.splitlines()[2]).groups())
    B = (Py - Fraction(Ay * Px, Ax)) * Fraction(Ax, (By * Ax - Bx * Ay))
    A = Fraction(Px - Bx * B, Ax)
    tokens2 = 3 * A + B
    if A.denominator == 1 and B.denominator == 1 and A >= 0 and B >= 0:
        total += tokens2.numerator
print(total)


total2 = 0
for m in machines.split("\n\n"):
    Ax, Ay = map(int, re.search(r"X\+(\d+), Y\+(\d+)", m.splitlines()[0]).groups())
    Bx, By = map(int, re.search(r"X\+(\d+), Y\+(\d+)", m.splitlines()[1]).groups())
    Px, Py = map(int, re.search(r"X\=(\d+), Y\=(\d+)", m.splitlines()[2]).groups())
    Px = Px + 10000000000000
    Py = Py + 10000000000000

    B = (Py - Fraction(Ay * Px, Ax)) * Fraction(Ax, (By * Ax - Bx * Ay))
    A = Fraction(Px - Bx * B, Ax)
    tokens2 = 3 * A + B
    if A.denominator == 1 and B.denominator == 1 and A >= 0 and B >= 0:
        total2 += tokens2.numerator
print(total2)
