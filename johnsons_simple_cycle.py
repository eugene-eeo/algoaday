from collections import defaultdict


def matrix_to_adjlist(M):
    A = defaultdict(list)
    for u, adj in enumerate(M):
        for v, weight in enumerate(adj):
            if weight > 0:
                A[u].append(v)
    return A


def subgraph(A, k):
    A_k = defaultdict(list)
    for u, row in A.items():
        if u >= k:
            for v in row:
                if v >= k:
                    A_k[u].append(v)
    return A_k


def empty_graph(A):
    return (not A) or all((not A[u]) for u in A)


def find_cycles(M):
    A = matrix_to_adjlist(M)    # adjacency list of M
    A_k = A                     # adjacency list of induced subgraph on nodes >= k of M
    B = {}                      # unblock map
    blocked = [False] * len(M)  # blocked nodes
    s = 0                       # min node
    n = max(A)
    stack = []
    cycles = []

    def unblock(u):
        blocked[u] = False
        for w in list(B[u]):
            B[u].remove(w)
            if blocked[w]:
                unblock(w)

    def circuit(v):
        f = False
        stack.append(v)
        blocked[v] = True

        for w in A_k[v]:
            if w == s:
                cycles.append(stack + [s])
                f = True
            elif not blocked[w]:
                if circuit(w):
                    f = True
        if f:
            unblock(v)
        else:
            for w in A_k[v]:
                B[w].add(v)
        assert stack.pop() == v
        return f

    while s < n:
        A_k = subgraph(A, s)
        if empty_graph(A_k):
            break
        s = min(A_k)
        for i in A_k:
            blocked[i] = False
            B[i] = set()
        circuit(s)
        s += 1
    return cycles
