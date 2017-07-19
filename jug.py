from collections import deque


def vectors_equal(A, B):
    for a, b in zip(A, B):
        if a is None or b is None:
            continue
        if a != b:
            return False
    return True


def fill_4(x, y):        return (4, y)
def fill_3(x, y):        return (x, 3)
def empty_4(x, y):       return (0, y)
def empty_3(x, y):       return (x, 0)
def fill_4_with_3(x, y): return (4, y - (4 - x))
def fill_3_with_4(x, y): return (x - (3 - y), 3)
def all_3_to_4(x, y):    return (min(x+y, 4), 0)
def all_4_to_3(x, y):    return (0, min(x+y, 3))


OPS = [
    fill_4,
    fill_3,
    empty_4,
    empty_3,
    fill_4_with_3,
    fill_3_with_4,
    all_3_to_4,
    all_4_to_3,
]


def verify(max_caps, vec):
    for limit, stored in zip(max_caps, vec):
        if stored > limit or stored < 0:
            return False
    return True


def find_path(initial, target, ops, max_caps):
    q = deque([([], initial)])
    while q:
        path, state = q.popleft()
        print(path, state)
        if vectors_equal(state, target):
            return path
        for op in ops:
            vec = op(*state)
            if vec != state and vec != initial and verify(max_caps, vec):
                q.append((
                    path + [op.__name__],
                    vec,
                ))
