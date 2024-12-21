with open("day19_input.txt") as f:
    towels, designes = f.read().split("\n\n")

towels = towels.split(", ")
designes = designes.splitlines()


def foo(des, towels, cached):
    if des in cached:
        return False
    if len(des) == 0:
        return True
    for t in towels:
        if des.startswith(t) and foo(des[len(t) :], towels, cached):
            return True
    cached.add(des)
    return False


print(len([d for d in designes if foo(d, towels, set())]))


def foo2(suffix, towels, cached):
    if suffix in cached:
        return cached[suffix]
    if len(suffix) == 0:
        return 1
    retval = 0
    for t in (t for t in towels if suffix.startswith(t)):
        retval += foo2(suffix[len(t) :], towels, cached)
    cached[suffix] = retval
    return retval


print(sum([foo2(d, towels, {}) for d in designes]))
