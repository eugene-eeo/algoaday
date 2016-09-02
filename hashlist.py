from hashlib import sha256
from itertools import chain


class Block:
    def __init__(self, content):
        self.hash = sha256(content).hexdigest()
        self.content = content


class HashList:
    def __init__(self, blocks):
        self.blocks = tuple(blocks)
        self.hashes = tuple(b.hash for b in self.blocks)

    def extend(self, blocks):
        return HashList(chain(self, blocks))

    def __eq__(self, other):
        return self.hashes == other.hashes


if __name__ == '__main__':
    h1 = HashList([
        Block(b'abc'),
        Block(b'def'),
        ])
    h2 = HashList([
        Block(b'abc'),
        ])
    assert h1 != h2
    assert h1 == h2.extend([Block(b'def')])
