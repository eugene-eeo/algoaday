from collections import deque


def find_path(G, src, dst):
    q = deque([[src]])
    while q:
        path = q.popleft()
        last = path[-1]
        if last == dst:
            return path
        for node, weight in enumerate(G[last]):
            if weight > 0 and node not in path:
                q.append(path + [node])


def edges_of_path(path):
    for i in range(len(path) - 1):
        yield path[i], path[i+1]


def make_flow_graph(C):
    F = [[0] * len(C) for _ in range(len(C))]
    return F


def make_residual_graph(C):
    R = [row[:] for row in C]
    return R


def edmonds_karp(C, src, dst):
    F = make_flow_graph(C)
    R = make_residual_graph(C)
    while True:
        path = find_path(R, src, dst)
        if path is None:
            break
        cap = min(R[u][v] for u, v in edges_of_path(path))
        for u, v in edges_of_path(path):
            R[u][v] -= cap
            R[v][u] += cap
            F[u][v] += cap
    return F


C = [
    # s, v1, v2, v3, v4,  t
    [ 0, 16, 13,  0,  0,  0], # s
    [ 0,  0, 10, 12,  0,  0], # v1
    [ 0,  4,  0,  0, 14,  0], # v2
    [ 0,  0,  9,  0,  0, 20], # v3
    [ 0,  0,  0,  7,  0,  4], # v4
    [ 0,  0,  0,  0,  0,  0], # t
]
