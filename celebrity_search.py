from random import randint, sample


def unique_pairs(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i + 1, size):
            yield i, j


def search(matrix):
    celebs = [1] * len(matrix)
    for x, y in unique_pairs(matrix):
        # 1. celebrity does not know anyone else. x knows y => x is not a celebrity.
        # 2. celebrity is known by all. x doesn't know y => y is not a celebrity.
        x_knows_y = matrix[x][y]
        y_knows_x = matrix[y][x]
        celebs[x if x_knows_y else y] = 0
        celebs[y if y_knows_x else x] = 0
    assert celebs.count(1) == 1
    return celebs.index(1)


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
    for n in range(5, 100, 5):
        matrix = random_matrix(n)
        celeb = search(matrix)
        assert all(v == 0 for v in matrix[celeb])
        for i, row in enumerate(matrix):
            if i != celeb:
                assert row[celeb]

        celeb = randint(0, n - 1)
        edges = random_adjacency_list(n, celeb)
        assert search_edges(edges) == celeb
