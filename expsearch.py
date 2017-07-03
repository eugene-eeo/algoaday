import bisect


def exponential_search(v, xs):
    size = len(xs)
    upper = 1
    while upper < size and xs[upper] < v:
        upper *= 2
    return bisect.bisect_left(xs, v,
            lo=upper // 2,
            hi=min(upper, size))


if __name__ == '__main__':
    for n in range(1, 20 + 1):
        a = list(range(n))
        for i, v in enumerate(a):
            assert exponential_search(v, a) == i
