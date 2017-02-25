class Leaf:
    def __init__(self, value):
        self.value = value

    def split_at(self, i):
        return (
            Leaf(self.value[:i]),
            Leaf(self.value[i:]),
            )

    def __add__(self, b):
        return Concat(self, b)

    def __getitem__(self, i):
        return self.value[i]

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        yield self

    def __repr__(self):
        return 'Leaf(%r)' % (self.value)


class Concat:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.length = len(left) + len(right)

    def __repr__(self):
        return 'Concat(%r, %r)' % (self.left, self.right)

    @property
    def value(self):
        return self.left.value + self.right.value

    def split_at(self, i):
        m = len(self.left)
        if i == m:
            return (self.left, self.right)
        elif i < m:
            l, r = self.left.split_at(i)
            return (l, r + self.right)
        else:
            l, r = self.right.split_at(i - m)
            return (self.left + l, r)

    def __iter__(self):
        yield from self.left
        yield from self.right

    def rebalance(self):
        S = []
        for node in self:
            size = 1
            while S:
                prev_node, prev_size = S.pop()
                if prev_node is node or prev_size != size:
                    S.append((prev_node, prev_size))
                    break
                size += prev_size
                node = Concat(prev_node, node)
            S.append((node, size))
        root, _ = S[0]
        for node, _ in S[1:]:
            root = Concat(root, node)
        return root

    #def rebalance(self):
    #    def balance(seq):
    #        while True:
    #            a = next(seq)
    #            b = next(seq, None)
    #            if b is None:
    #                yield a
    #                break
    #            yield Concat(a, b)
    #    rv = self
    #    while True:
    #        rv = list(balance(iter(rv)))
    #        if len(rv) == 1:
    #            return rv[0]

    def __add__(self, b):
        return Concat(self, b)

    def _substring(self, a, b):
        _, r = self.split_at(a)
        return r.split_at(b - a)[0]

    def __getitem__(self, i):
        if isinstance(i, slice):
            start, stop, step = i.indices(len(self))
            assert step == 1
            assert stop >= start
            return self._substring(start, stop)
        return (
            self.left[i] if i < len(self.left) else
            self.right[i - len(self.left)]
            )

    def __len__(self):
        return self.length


def length(node):
    if isinstance(node, Leaf):
        return 1
    return length(node.left) + length(node.right)


def depth(node):
    if isinstance(node, Leaf):
        return 0
    return 1 + max(depth(node.left), depth(node.right))


def fibo(n, m={0: 1, 1: 1}):
    if n not in m:
        m[n] = fibo(n-1) + fibo(n-2)
    return m[n]


def balanced(rope):
    d = depth(rope)
    return length(rope) >= fibo(d + 1)


if __name__ == '__main__':
    r = Concat(
        Concat(Leaf('a'), Leaf('b')),
        Concat(
            Leaf('c'),
            Concat(
                Leaf('d'),
                Concat(Leaf('e'), Leaf('f'))
                )))

    assert r.value == 'abcdef'
    for i, char in enumerate(r.value):
        assert r[i] == char

    v = r.value
    for i in range(len(r)):
        left, right = r.split_at(i)
        assert left.value == v[:i]
        assert right.value == v[i:]

    for i in range(len(r)):
        for j in range(i, len(r)):
            assert r[i:j].value == v[i:j]

    assert r.rebalance().value == r.value
    assert length(r.rebalance()) == length(r)
    assert balanced(r.rebalance())
    assert not balanced(r)
    assert depth(r) == 4
