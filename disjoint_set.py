# Disjoint Set Datastructure
# Represent elements as nodes.
# Initially the elements are not part of any tree:
#
#  [ {1} ]  [ {2} ]  [ {3} ]
#
# To union 2 sets we have to attach one to another:
#
#      [{1}]              [{1}] and [{2}] have same root ([{1}])
#         \               so they are part of the same set!
#        [{2}]  [{3}]
#
# To make future searches fast we perform fixups when
# we search (path compression:
#
#     [{1}]                    [{1}]                     [{1}]
#       |        Find(4)       /   \       Find(3)       / | \
#     [{2}]     --------> [{2}]    [{4}]  ---------> [{2}] |  [{4}]
#     /   \                 |                              |
#  [{3}] [{4}]            [{3}]                          [{3}]
#
# This is ok because they still have the same root.


class Node:
    def __init__(self, x, parent, rank):
        self.x = x
        self.parent = parent
        self.rank = rank


def make_set(x):
    node = Node(x, None, 0)
    node.parent = node
    return node


def find(x):
    while x.parent is not x:
        x, x.parent = x.parent, x.parent.parent
    return x.parent


def union(x, y):
    # find the roots
    x = find(x)
    y = find(y)
    if x is y:
        return

    # make sure x.rank >= y.rank
    # then attach y to x
    if x.rank < y.rank:
        x, y = y, x

    y.parent = x
    if x.rank == y.rank:
        x.rank += 1


if __name__ == '__main__':
    x = make_set(1)
    y = make_set(2)
    z = make_set(3)
    t = make_set(4)

    union(x, y)
    assert find(x) == find(y)
    assert find(x) != find(z)

    union(x, z)
    assert find(x) == find(z)
    assert find(y) == find(z)
