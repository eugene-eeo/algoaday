from random import randint, sample


def search(matrix):
    celebs = list(range(len(matrix)))
    while len(celebs) >= 2:
        x = celebs.pop()
        y = celebs.pop()
        celebs.append(y if matrix[x][y] else x)
    assert len(celebs) == 1
    return celebs[0]


def random_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    celeb = randint(0, n-1)
    # make the nodes know each other, except for the
    # celebrity because celebrity by definition knows
    # no other nodes.
    for i in range(n):
        if i == celeb:
            continue
        peers = sample([u for u in range(n) if u != i], randint(1, n-1))
        for j in peers:
            matrix[i][j] = 1
        matrix[i][celeb] = 1
    return matrix


def random_adjacency_list(n, celeb):
    for i in range(n):
        if i == celeb:
            continue
        peers = sample([u for u in range(n) if u != i and u != celeb],
                       randint(1, n-2))
        yield i, celeb
        for j in peers:
            yield i, j


def search_edges(edges):
    celebs = set()
    normal = set()
    for a, b in edges: # a knows b
        celebs.discard(a)
        normal.add(a)
        if b not in normal:
            celebs.add(b)
    assert len(celebs) == 1
    return celebs.pop()


if __name__ == '__main__':
    matrix = random_matrix(5)
    celeb = search(matrix)
    assert all(v == 0 for v in matrix[celeb])
    for i, row in enumerate(matrix):
        if i != celeb:
            assert row[celeb]

    celeb = randint(0, 5 - 1)
    edges = random_adjacency_list(5, celeb)
    assert search_edges(edges) == celeb
