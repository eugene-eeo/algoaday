from fractions import Fraction


def find_nonzero(M, col, min_row):
    for i, row in enumerate(M):
        if i >= min_row and row[col] != 0:
            return i


def multiply(v, A):
    return [u*v for u in A]


def subtract(A, B):
    return [a - b for a, b in zip(A, B)]


def gj_elim(M):
    n = len(M)
    for col in range(n):
        # find the first row with a nonzero column after
        # the previous row, swap with the col-th row
        idx = find_nonzero(M, col, col)
        M[idx], M[col] = M[col], M[idx]

        # multiply with a value such that it will make the
        # col-th column on the current row == 1
        M[col] = multiply(1 / M[col][col], M[col])
        assert M[col][col] == 1

        # make the col-th column == 0 on all other rows
        for i in range(n):
            if i == col:
                continue
            M[i] = subtract(
                M[i],
                multiply(M[i][col], M[col])
            )
            assert M[i][col] == 0
    return M


def solve(M):
    rref = gj_elim(M)
    return [row[-1] for row in M]


def fractionify(M):
    return [[Fraction(u) for u in row] for row in M]


if __name__ == '__main__':
    matrix = [
        [3, 1, 0, 5],
        [0, 2, 0, 7],
        [0, 1, 1, 14],
    ]
    fractionify(matrix)
    assert solve(matrix) == [0.5, 3.5, 10.5]
