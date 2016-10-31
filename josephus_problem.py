import math


def left(a, i):
    return (i+1) % len(a)


def w(n):
    s = list(range(1, n+1))
    c = 0
    while len(s) != 1:
        i = left(s, c)
        del s[i]
        c = i % len(s)
    return s[0]


def residue(n):
    return n - 2**int(math.log2(n))


def w2(n):
    return 2*residue(n) + 1


if __name__ == '__main__':
    values = [1, 1, 3, 1, 3, 5, 7, 1, 3, 5, 7, 9]
    for n, v in enumerate(values, 1):
        assert w(n) == w2(n) == v

    for n in range(100, 200):
        assert w(n) == w2(n)
