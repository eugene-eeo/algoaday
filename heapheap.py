import math
from random import randint


def heapheap(xs):
    h = math.ceil(math.log2(len(xs)))
    n = int(math.pow(2, h))
    # so we can start indexing at 1
    H = [None]
    H.extend(0 for _ in range(n - 1))
    H.extend(xs)
    H.extend(0 for _ in range(n - len(xs)))
    for i, v in enumerate(xs):
        update(H, i, v)
    return H


def update(heap, i, v):
    # full heap is always of size n = 2^h - 1
    # so log(n + 1) gives us h
    h = int(math.log2(len(heap)))
    _update(heap,
           int(math.pow(2, h - 1)) + i,
           v)
    return heap[1]


def _update(heap, i, v):
    heap[i] = v
    if i != 1:
        p = i // 2
        l = 2*p
        r = 2*p + 1
        _update(heap,
                p,
                heap[l] + heap[r])


if __name__ == '__main__':
    for _ in range(100):
        n = randint(4, 10)
        xs = [randint(1, 10) for _ in range(n)]
        heap = heapheap(xs)
        for _ in range(20):
            i = randint(0, n - 1)
            v = randint(1, 10)
            xs[i] = v
            assert update(heap, i, v) == sum(xs)
