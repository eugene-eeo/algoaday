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
    for i in range(n):
        # find the first row with a nonzero column after
        # the previous row, swap with the i-th row
        idx = find_nonzero(M, i, i)
        M[idx], M[i] = M[i], M[idx]

        # multiply with a value such that it will make the
        # i-th column on the current row == 1
        M[i] = multiply(1 / M[i][i], M[i])
        assert M[i][i] == 1

        # make the i-th column == 0 on all other rows
        for j in range(n):
            if j == i:
                continue
            M[j] = subtract(
                M[j],
                multiply(M[j][i], M[i]),
            )
            assert M[j][i] == 0
    return M


def solve(M):
    gj_elim(M)
    return [row[-1] for row in M]


def fractionify(M):
    return [[Fraction(u) for u in row] for row in M]


if __name__ == '__main__':
    matrix = fractionify([
        [3, 1, 0, 5],   # 3x + 1y + 0z = 5
        [0, 2, 0, 7],   # 0x + 2y + 0z = 7
        [0, 1, 1, 14],  # 0x + 1y + 1z = 14
    ])
    assert solve(matrix) == [0.5, 3.5, 10.5]
