def forward_substitution(L, b):
    n = len(L)
    y = [0] * n
    for i in range(n):
        y[i] = b[i][0]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]
    return y

def backward_substitution(U, y):
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x

def lu_decomposition(mat_a):
    n = len(mat_a)
    lower = [[0.0] * n for _ in range(n)]
    upper = [[0.0] * n for _ in range(n)]

    for i in range(n):
        lower[i][i] = 1.0

    for i in range(n):
        # upper triangler
        for k in range(i, n):
            sum = 0.0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
            upper[i][k] = mat_a[i][k] - sum

        # lower triangle
        for k in range(i, n):
            if i == k:
                lower[k][i] = 1.0  # diagonal
            else:
                sum = 0.0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
                lower[k][i] = (mat_a[k][i] - sum) / upper[i][i]

    return lower, upper

def lu_solve(mat_a, b):
    L, U = lu_decomposition(mat_a)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

