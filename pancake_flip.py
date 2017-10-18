def nds(xs):
    p = 0
    q = len(xs) - 1
    for i, _ in enumerate(xs):
        if i == q:
            return (-1, -1)
        if xs[i] > xs[i+1]:
            p = i
            break
    for i, _ in enumerate(xs[p+1:], p+1):
        if xs[i-1] < xs[i]:
            q = i - 1
            break
    return p, q


def is_sorted(xs):
    for i in range(1, len(xs)):
        if xs[i-1] > xs[i]:
            return False
    return True


def flip(xs, k):
    for i in range((k + 1) // 2):
        xs[i], xs[k-i] = xs[k-i], xs[i]


# xs = [1, 2, 5, 4, 3, 6, ...]
# => [1, 2, (5, 4, 3), 6, ...] identify nds
# => [(3, 4, 5), 2, 1, 6, ...] flip at nds end
# => [(5, 4, 3), 2, 1, 6, ...] flip at nds end-start
# => [1, 2, (3, 4, 5), 6, ...]
def sort(xs):
    while not is_sorted(xs):
        start, end = nds(xs)
        flip(xs, end)
        flip(xs, end - start)
        flip(xs, end)
        assert is_sorted(xs[start:end+1])
    return xs


# rsort(xs, pre)
# try to sort longer and longer prefixes of the
# array:
#  - xs = A[1..n]
#  - pre= A[1..m] where m <= n
#
def rsort(xs, pre=[]):
    if len(xs) == len(pre):
        return xs
    L = len(pre)
    m = min(xs[L:])
    if xs[:L + 1] != pre + [m]:
        i = xs.index(m)
        flip(xs, i)
        if pre:
            flip(xs, i - L)
            flip(xs, i)
    return rsort(xs, pre + [m])


if __name__ == '__main__':
    from itertools import permutations
    for k in range(1, 6):
        for xs in permutations(range(k)):
            xs = list(xs)
            xd = xs[:]
            assert is_sorted(rsort(xs))
            assert is_sorted(sort(xd))
