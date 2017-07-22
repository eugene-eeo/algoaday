def itoset(i):
    return 1 << i


def from_seq(xs):
    u = 0
    for item in xs:
        if item < 0:
            raise ValueError
        u = union(u, itoset(item))
    return u


intersection         = int.__and__
union                = int.__or__
symmetric_difference = int.__xor__


def contains(iset, i):
    z = itoset(i)
    return intersection(iset, z) == z


def discard(iset, i):
    if contains(iset, i):
        return symmetric_difference(iset, itoset(i))
    return iset


def difference(a, b):
    return symmetric_difference(a, intersection(a, b))


if __name__ == '__main__':
    xs = {1, 4, 5}
    z = from_seq(xs)
    for i in xs:
        assert contains(z, i)

    assert not contains(z, 0)
    assert not contains(z, 6)

    assert intersection(z, from_seq({1, 3, 6})) == from_seq(xs & {1, 3, 6})
    assert union(z, from_seq({2, 4, 5})) == from_seq(xs | {2, 4, 5})
    assert symmetric_difference(
        from_seq({1, 2, 3}),
        from_seq({3, 4, 5}),
        ) == from_seq({1, 2, 3}.symmetric_difference({3, 4, 5}))

    assert discard(z, 1) == from_seq([4, 5])
    assert difference(
            from_seq([1, 2, 3]),
            from_seq([3, 4, 5]),
        ) == from_seq([1, 2])
