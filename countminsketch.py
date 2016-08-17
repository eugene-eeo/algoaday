import fnvhash


DEFAULT = [
    fnvhash.fnv0_32,
    fnvhash.fnv1_32,
    fnvhash.fnv1a_32,
]


class CountMinSketch:
    def __init__(self, width, algos=DEFAULT):
        self.width = width
        self.algos = algos
        self.array = []
        for _ in range(len(algos)):
            self.array.append([0] * width)

    def insert(self, elem):
        for index, algo in enumerate(self.algos):
            row = self.array[index]
            row[algo(elem) % self.width] += 1

    def count(self, elem):
        m = []
        for index, algo in enumerate(self.algos):
            row = self.array[index]
            m.append(row[algo(elem) % self.width])
        return min(m)


if __name__ == '__main__':
    cms = CountMinSketch(20)
    cms.insert(b'abc')
    cms.insert(b'def')
    cms.insert(b'def')

    assert cms.count(b'abc') == 1
    assert cms.count(b'def') == 2
