import fnvhash

DEFAULT = [
    fnvhash.fnv0_32,
    fnvhash.fnv1_32,
    fnvhash.fnv1a_32,
]


class BloomFilter(object):
    def __init__(self, algorithms=DEFAULT, space=100):
        self.algorithms = tuple(algorithms)
        self.array = [False for _ in range(space)]
        self.space = space

    def __contains__(self, item):
        return all(
            self.array[algo(item) % self.space]
            for algo in self.algorithms
            )

    def insert(self, item):
        for algo in self.algorithms:
            self.array[algo(item) % self.space] = 1


if __name__ == '__main__':
    bf = BloomFilter()
    bf.insert(b'abc')
    bf.insert(b'def')

    assert b'abc' in bf
    assert b'def' in bf
    assert b'cde' not in bf
