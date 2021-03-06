import random


def breakdown(S):
    """
    Given S, a sum of unique powers of two, e.g.
    2^0 + 2^4 + 2^7, returns an array of the exponents.
    """
    shift = 0
    factors = []
    while S != 0:
        if S % 2 == 1:
            S -= 1
            factors.append(shift)
        S = S / 2
        shift += 1
    return factors


def rbreakdown(S, k=0):
    if S == 0:
        return
    if S % 2 == 1:
        yield k
        yield from rbreakdown(S - 1, k)
        return
    yield from rbreakdown(S / 2, k + 1)


if __name__ == '__main__':
    for _ in range(1000):
        u = random.randint(1, 12)
        arr = {random.randint(1, 20) for _ in range(u)}
        S = sum(2**k for k in arr)
        assert set(breakdown(S)) == arr
