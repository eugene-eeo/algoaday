from fnvhash import fnv0_32


def mean(xs):
    return sum(xs) // float(len(xs))


def split_bits(number, n):
    b = bin(number)[2:]
    return b[:n], b[n:]


class LogLog:
    prefix_size = 10

    def __init__(self):
        self.buckets = [0] * 2**self.prefix_size

    def insert(self, item):
        h = fnv0_32(item)
        head, tail = split_bits(h, self.prefix_size)
        head = int(head, base=2)
        self.buckets[head] = max(
            self.buckets[head],
            len(tail) - len(tail.rstrip('1')) + 1,
            )

    def cardinality(self):
        xs = [k-1 for k in self.buckets if k > 0]
        if not xs:
            return 0
        return 2**mean(xs)


if __name__ == '__main__':
    mset = LogLog()
    mset.insert(b'abc')
    mset.insert(b'jkl')
    assert mset.cardinality() == 2.0
