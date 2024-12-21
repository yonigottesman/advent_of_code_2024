import re

with open("day17_input.txt") as f:
    reg, program = f.read().split("\n\n")

registers = dict([(r, int(v)) for r, v in re.findall(r"Register ([ABC]): (\d+)", reg)])
registers["ip"] = 0
program = list(map(int, program.split(" ")[1].split(",")))
output = []
combo = {
    0: lambda: 0,
    1: lambda: 1,
    2: lambda: 2,
    3: lambda: 3,
    4: lambda: registers["A"],
    5: lambda: registers["B"],
    6: lambda: registers["C"],
}


def adv(operand):
    registers["A"] = int(registers["A"] / pow(2, combo[operand]()))


def bxl(operand):
    registers["B"] = registers["B"] ^ operand


def bst(operand):
    registers["B"] = combo[operand]() % 8


def jnz(operand):
    if registers["A"] != 0:
        registers["ip"] = operand
        return True
    else:
        return False


def bxc(operand):
    registers["B"] = registers["B"] ^ registers["C"]


def out(operand):
    output.append(combo[operand]() % 8)


def bdv(operand):
    registers["B"] = int(registers["A"] / pow(2, combo[operand]()))


def cdv(operand):
    registers["C"] = int(registers["A"] / pow(2, combo[operand]()))


opcode_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

while registers["ip"] < len(program):
    opcode, operand = program[registers["ip"]], program[registers["ip"] + 1]
    jumped = opcode_map[opcode](operand)
    if not jumped:
        registers["ip"] = registers["ip"] + 2
print(",".join(map(str, output)))
print(registers)


import re

with open("day17_input.txt") as f:
    reg, program = f.read().split("\n\n")

registers = dict([(r, int(v)) for r, v in re.findall(r"Register ([ABC]): (\d+)", reg)])
registers["ip"] = 0
program = list(map(int, program.split(" ")[1].split(",")))
output = []
combo = {
    0: lambda: 0,
    1: lambda: 1,
    2: lambda: 2,
    3: lambda: 3,
    4: lambda: registers["A"],
    5: lambda: registers["B"],
    6: lambda: registers["C"],
}


def adv(operand):
    registers["A"] = int(registers["A"] / pow(2, combo[operand]()))


def bxl(operand):
    registers["B"] = registers["B"] ^ operand


def bst(operand):
    registers["B"] = combo[operand]() % 8


def jnz(operand):
    if registers["A"] != 0:
        registers["ip"] = operand
        return True
    else:
        return False


def bxc(operand):
    registers["B"] = registers["B"] ^ registers["C"]


def out(operand):
    output.append(combo[operand]() % 8)


def bdv(operand):
    registers["B"] = int(registers["A"] / pow(2, combo[operand]()))


def cdv(operand):
    registers["C"] = int(registers["A"] / pow(2, combo[operand]()))


opcode_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

iss = []
for i in range(1000):
    start = 202975183645226  # 31451369712170 + i * 4398046511104 looked for some patterns and
    registers["A"] = start
    registers["B"] = 0
    registers["C"] = 0
    registers["ip"] = 0
    last_output = 0
    output.clear()

    while registers["ip"] < len(program):
        opcode, operand = program[registers["ip"]], program[registers["ip"] + 1]
        jumped = opcode_map[opcode](operand)
        if not jumped:
            registers["ip"] = registers["ip"] + 2

        if opcode == 5:
            if program[last_output] != output[-1]:
                break
            last_output += 1
        if len(output) > 15:
            if (start) not in iss:
                iss.append(start)
                print(start)
    break
print(",".join(map(str, output)))  # 202975183645226
