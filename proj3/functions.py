import matplotlib.pyplot as plt

from pandas import read_csv


DATA_DIR = "data/"
MEDIA_DIR = "sprawozdanie/media/"
PROFILE1 = "easy"
PROFILE2 = "medium"
PROFILE3 = "hard"


def read_profile(filename):
    records = read_csv(DATA_DIR + filename + ".csv").values
    distances = [record[0] for record in records]
    elevations = [record[1] for record in records]
    return distances, elevations


def draw_profile(filename):
    distances, elevations = read_profile(filename)
    plt.plot(distances, elevations)
    plt.show()


def linspace(start, stop, n):
    if n == 1:
        yield stop
        return
    h = (stop - start) / (n - 1)
    for i in range(n):
        yield start + h * i

def interpolate_lagrange(x, X, Y):
    n = len(X)
    result = 0.0
    for i in range(n):
        term = Y[i]
        for j in range(n):
            if i != j:
                ratio = (x - X[j]) / (X[i] - X[j])
                term *= ratio
        result += term

    return result

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



def evenly_spaced_plots(filename, title, interpolations=(6, 9, 15, 20), interp_function=lagrange):
    X, Y = read_profile(filename)

    _, axis = plt.subplots(len(interpolations), figsize=(8,12), constrained_layout=True)
    plt.suptitle(f"{title}")
    for num_axis,i in enumerate(interpolations):
        x, y, ixs = interp_function(X, Y, num_interpolation=i)
        axis[num_axis].set_title(f"{i} punktów węzłowych")
        axis[num_axis].set_xlabel("odległość [m]")
        axis[num_axis].set_ylabel("wysokość [m]")
        axis[num_axis].plot(X, Y)
        axis[num_axis].plot(x, y)
        axis[num_axis].scatter([X[i] for i in ixs], [Y[i] for i in ixs], c='g')
        axis[num_axis].legend(["dane", "interpolacja", "punkty węzłowe"])

    plt.show()


def plots_specific_indexes(filename, title, indexes, interp_function=lagrange):
    X, Y = read_profile(filename)
    x, y, ixs = interp_function(X, Y, indexes=indexes)

    plt.title(f"nierównomierne punkty węzłowe: {title}")
    plt.xlabel("odległość [m]")
    plt.ylabel("wysokość [m]")
    plt.plot(X, Y)
    plt.plot(x, y)
    plt.scatter([X[i] for i in ixs], [Y[i] for i in ixs], c='g')
    plt.legend(["dane", "interpolacja", "punkty węzłowe"])

    plt.show()

def generate_czebyszew(N, data_size):
    import math
    def fu(k):
        return data_size/2 * math.cos((2 * k + 1)/(2 * N) * math.pi) + data_size/2
    return [int(fu(k)) for k in range(N-1, -1, -1)] + [data_size]
