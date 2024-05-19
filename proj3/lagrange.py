from numpy import linspace

def lagrange_polynomial(x, indexes, X, Y):
    result = 0
    for i in indexes:
        term = Y[i]
        for j in indexes:
            if i != j:
                term *= (x - X[j]) / (X[i] - X[j])
        result += term
    return result

def lagrange(X, Y, num_interpolation=9, num_evaluated=1000, indexes=None):
    if indexes is None:
        indexes = [int(i) for i in linspace(0, len(X) - 1, num_interpolation)]
    interpolated_X = list(linspace(X[0], X[-1], num_evaluated))
    interpolated_Y = [lagrange_polynomial(x, indexes, X, Y) for x in interpolated_X]
    return interpolated_X, interpolated_Y, indexes

