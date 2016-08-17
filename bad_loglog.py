from random import random
from fnvhash import fnv0_32
import string


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
            len(tail) - len(tail.lstrip('1')) + 1,
            )

    def cardinality(self):
        return sum(2 ** (m-1) if m > 0 else 0 for m in self.buckets)


if __name__ == '__main__':
    mset = LogLog()
    for char in string.ascii_letters:
        mset.insert(char.encode())
    assert mset.cardinality() == len(string.ascii_letters)
