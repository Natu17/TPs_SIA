import math

dataset = [
    [(4.4793, -4.075, -4.075), 0],
    [(-4.1793, -4.9218, 1.7664), 1],
    [(-3.9439, -0.7689, 4.8830), 1],
]


def g(x):
    try:
        return math.e**x/(1+math.e**x)
    except OverflowError:
        return 1


def F(W, w, w0, E):
    return g(sum(
        W[j+1]*g(sum(
            w[j][k]*E[k]
            for k in range(0, 3)
        ) - w0[j])
        for j in range(0, 2)
    ) - W[0])


def E(W, w, w0):
    return sum((OUT - F(W, w, w0, IN))**2 for (IN, OUT) in dataset)

def error(planar_vec):
    W = (planar_vec[0:3])
    w = ((planar_vec[3:6]), (planar_vec[6:9]))
    w0 = (planar_vec[9:11])
    return E(W, w, w0)


def convert(planar):
    W = (planar[0:3])
    w = ((planar[3:6]), (planar[6:9]))
    w0 = (planar[9:11])
    return W, w, w0