import random
import bisect


def exponential_search(v, xs):
    size = len(xs)
    bound = 1
    while bound < size and xs[bound] < v:
        bound *= 2
    return bisect.bisect_left(xs, v,
            lo=bound // 2,
            hi=min(bound, size))


if __name__ == '__main__':
    a = [i for i in range(random.randint(1, 20))]
    for i, v in enumerate(a):
        assert exponential_search(v, a) == i
