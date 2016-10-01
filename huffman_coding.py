from collections import namedtuple


Node = namedtuple('Node', 'value,prob,children')


def pnode(probs):
    nodes = [Node(k, p, []) for k, p in probs.items()]
    if not nodes:
        return

    while len(nodes) != 1:
        nodes.sort(
            key=lambda node: node.prob,
            reverse=True,
            )
        a, b = nodes.pop(), nodes.pop()
        node = Node(None, a.prob + b.prob, [a, b])
        nodes.append(node)

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
