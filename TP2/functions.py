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


def error(genotype):
    W = (genotype[0:3])
    w = ((genotype[3:6]), (genotype[6:9]))
    w0 = (genotype[9:11])
    return E(W, w, w0)


import sys
MAX = sys.maxsize
DECAY = -math.log(1/MAX)
def fitness(genotype):
    #return MAX*math.exp(-DECAY*error(genotype))
    try:
        return 1/(error(genotype))
    except ZeroDivisionError:
        return math.inf
    #return len(dataset)-error(genotype)

