from random import choice, randint
import string

#
# levenshtein distance
# runtime: O(len(a) * len(b))
# properties:
#  - dist(a, b) == dist(b, a)
#  - dist(a, b) >= abs(len(a) - len(b))
#  - dist(a, b) <= max(len(a), len(b))
#  - dist(a, b) == 0 iff a == b
#  - dist(a, b) + dist(b, c) >= dist(a, c)


def lvdist(a, b, i=None, j=None):
    i = len(a) if i is None else i
    j = len(b) if j is None else j
    if min(i, j) == 0:
        return max(i, j)

    cost = 0
    if a[i-1] != b[j-1]:
        cost = 1

    return min(
        lvdist(a, b, i-1, j) + 1,  # delete from a
        lvdist(a, b, i, j-1) + 1,  # insert a character to b
        lvdist(a, b, i-1, j-1) + cost,  # (mis)match
        )


def lvdist2(a, b):
    d = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    for i in range(1, len(a)+1):
        d[i][0] = i  # if min(i, j) == 0: max(i, j)

    for j in range(1, len(b)+1):
        d[0][j] = j  # if min(i, j) == 0: max(i, j)

    for j in range(1, len(b)+1):
        for i in range(1, len(a)+1):
            if a[i-1] == b[j-1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(
                d[i-1][j] + 1,
                d[i][j-1] + 1,
                d[i-1][j-1] + cost,
            )
    return d[len(a)][len(b)]


def rsg():
    def getstr(s):
        return ''.join([
            choice(s) for _ in range(randint(1, 10))
        ])

    chars = string.ascii_letters
    for _ in range(20):
        yield getstr(chars), getstr(chars)


if __name__ == '__main__':
    for impl in [lvdist, lvdist2]:
        for a, b in rsg():
            try:
                dist = impl(a, b)
                assert dist == impl(b, a)
                assert dist >= abs(len(a) - len(b))
                assert dist <= max(len(a), len(b))
                if a == b:
                    assert dist == 0
                assert impl(a, "sub") + impl("sub", b) >= dist
            except AssertionError:
                print(impl.__name__, a, b)
                exit(1)
