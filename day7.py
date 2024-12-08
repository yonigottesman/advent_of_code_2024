def foo(equation, i, dest, agg):
    if dest == agg and i == len(equation):
        return True
    if agg > dest or i >= len(equation):
        return False

    return (
        foo(equation, i + 1, dest, agg + equation[i])
        or foo(equation, i + 1, dest, agg * equation[i])
        or foo(equation, i + 1, dest, int(str(agg) + str(equation[i])))
    )


with open("day7_input.txt") as f:
    lines = f.read().splitlines()
count = 0
for l in lines:
    test, equation = l.split(":")
    test = int(test)
    equation = [int(i) for i in equation.split()]
    if foo(equation, 1, test, equation[0]):
        count += test
print(count)
