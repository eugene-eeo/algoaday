def nqueens(n):
    def rnq(Q, r):
        if r == n + 1:
            yield tuple(Q)
            return
        for j in range(1, n+1):
            legal = True
            for i in range(1, r):
                ds = r - i
                v = Q[i-1]
                # horizontal attacks or along the diagonal
                if v == j or (v == j + ds) or (v == j - ds):
                    legal = False
            if legal:
                Q[r-1] = j
                yield from rnq(Q, r+1)
    return rnq([0] * n, 0)


if __name__ == '__main__':
    # table of values taken from http://web.math.ucsb.edu/~padraic/ucsb_2014_15/ccs_problem_solving_w2015/N-Queens%20presentation.pdf
    values = {
        1: 1,
        2: 0,
        3: 0,
        4: 2,
        5: 10,
        6: 4,
        7: 40,
        8: 92,
        9: 352,
    }
    for k, v in values.items():
        assert len(set(nqueens(k))) == v
