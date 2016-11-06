from heapq import heappush, heappop, heapify
from collections import namedtuple


class Node(namedtuple('Node', 'prob,value,children')):
    def __lt__(self, other):
        return self.prob < other.prob


def pnode(probs):
    nodes = [Node(p, x, []) for x, p in probs.items()]
    if not nodes:
        return
    heapify(nodes)
    while len(nodes) != 1:
        a, b = heappop(nodes), heappop(nodes)
        heappush(nodes, Node(a.prob + b.prob, None, [a, b]))
    return nodes[0]


def codes(node, prefix=()):
    if node.value is not None:
        yield node.value, prefix
        return
    left, right = node.children
    yield from codes(left, prefix + (0,))
    yield from codes(right, prefix + (1,))


if __name__ == '__main__':
    r = dict(codes(pnode({
        'a': 0.5,
        'b': 0.25,
        'c': 0.125,
        'd': 0.125,
    })))
    assert len(r['a']) == 1
    assert len(r['b']) == 2
    assert len(r['c']) == 3
    assert len(r['d']) == 3
