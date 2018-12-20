# Array x is bitonic iff there exists a unique i,j s.t.
#
#   x[i-1 % n] > x[i] < x[i+1 % n] and,
#   x[j-1 % n] < x[j] > x[j+1 % n]
#
# i.e. x is made of a descending and ascending sequence,
# or can be circularly shifted to be one.
# How to find min(x) in O(log n) time?

def find_min(xs):
    n = len(xs)
    i = 0       # start of asc
    d = n // 2  # step
    j = 0
    while d > 0:
        j += 1
        l = xs[(i-1) % n]
        c = xs[i     % n]
        r = xs[(i+1) % n]
        if l > c and c < r: break
        if l < c < r:       i -= d
        else:               i += d
        d = max(1, d // 2)
    return i % n


if __name__ == '__main__':
    for i in range(20):
        for j in range(20):
            if i == j == 0:
                continue
            u = list(range(i))
            v = list(range(i, i+j))[::-1]
            for j in range(0, 11):
                z = u + v
                z = z[j:] + z[:j]
                assert find_min(z) == z.index(0)
