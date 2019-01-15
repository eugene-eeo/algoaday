def lsb(i):
    return i & (-i)


def ft_sum(xs, i):
    assert i >= 1
    # query lower nodes about our sum
    # parent(i) = i - lsb(i)
    #    val(i) = sum( xs[parent(i)+1]...xs[i] )
    s = 0
    while i > 0:
        s += xs[i]
        i -= lsb(i)
    return s


def ft_add(xs, i, v):
    assert i >= 1
    # lower nodes can't be responsible for keeping track of
    # partial sum, so we only update upwards and find nodes
    # interested in our value
    n = len(xs)
    while i < n:
        xs[i] += v
        i += lsb(i)


if __name__ == '__main__':
    xs = [0] * (16 + 1)
    for i in range(1, 17):
        ft_add(xs, i, i)
    for i in range(i, 17):
        assert ft_sum(xs, i) == i*(i+1)/2
