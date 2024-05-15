from numpy import linspace
from lu import lu_solve

def splines(X, Y, num_interpolation=15, num_evaluated=1000, indexes=None):
    if indexes is None:
        indexes = [int(i) for i in linspace(0, len(X) - 1, num_interpolation)]
    n = len(indexes)
    a = [Y[ix] for ix in indexes]
    b = []
    d = []
    h = [X[indexes[i+1]] - X[indexes[i]] for i in range(n-1)]
    A = [[0 for _ in range(n)] for _ in range(n)]
    vec = [[0] for _ in range(n)]
    for i in range(1, n-1):
        A[i][i] = 2 * (h[i-1] + h[i])
        A[i][i-1] = h[i-1]
        A[i][i+1] = h[i]
        vec[i][0] = 3 * ((Y[indexes[i+1]] - Y[indexes[i]])/h[i] - \
                         (Y[indexes[i]] - Y[indexes[i-1]])/h[i-1])
    A[0][0] = 1
    A[n-1][n-1] = 1
    c = lu_solve(A, vec)
    for i in range(n-1):
        d.append((c[i+1] - c[i])/(3 * h[i]))
        b.append((Y[indexes[i+1]] - Y[indexes[i]])/h[i] - h[i]/3 * (2 * c[i] + c[i+1]))
    b.append(0)
    d.append(0)
    def F(x):
        ix = n-1
        for ix_num in range(len(indexes) - 1):
            if X[indexes[ix_num]] <= x < X[indexes[ix_num + 1]]:
                ix = ix_num
                break
        h = x-X[indexes[ix]]
        return a[ix] + b[ix] * h + c[ix] * h**2 + d[ix] * h ** 3
    interpolated_X = list(linspace(X[0], X[-1], num_evaluated))
    interpolated_Y = [F(x) for x in interpolated_X]
    return interpolated_X, interpolated_Y, indexes
