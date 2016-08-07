import fnvhash

DEFAULT = [
    fnvhash.fnv0_32,
    fnvhash.fnv1_32,
    fnvhash.fnv1a_32,
]


class BloomFilter(object):
    def __init__(self, algorithms=DEFAULT, space=100):
        self.algorithms = tuple(algorithms)
        self.storage = [False for _ in range(space)]
        self.space = space

    def __contains__(self, item):
        return all(
            self.storage[algo(item) % self.space]
            for algo in self.algorithms
            )

    def add(self, item):
        for algo in self.algorithms:
            self.storage[algo(item) % self.space] = 1

    def confidence(self):
        return 1 - sum(self.storage) / self.space


if __name__ == '__main__':
    bf = BloomFilter()
    bf.add(b'abc')
    bf.add(b'def')

    assert b'abc' in bf
    assert b'def' in bf
    assert b'cde' not in bf
