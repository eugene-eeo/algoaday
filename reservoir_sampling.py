import random


def sample(s, k):
    res = []
    for n, item in enumerate(s, 1):
        if n <= k:
            res.append(item)
        elif random.random() < k/(n+1.0):
            i = random.randint(0, k-1)
            res[i] = item
    return res


if __name__ == '__main__':
    rand = [i for i in range(1, 101)]
    for i in range(1, 50):
        assert len(sample(rand, i)) == i
