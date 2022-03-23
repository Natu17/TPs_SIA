import math
import random
import argparse


GENOTYPE_LEN = 11

parser = argparse.ArgumentParser("Solving function optimization with genetic algorithms")
parser.add_argument("--population", dest="population", default="500", help="Population size")
parser.add_argument("--seed", dest="seed", default="0", help="Seed for random generator")

args = parser.parse_args()

P = int(args.population)
RANDOM_SEED = int(args.seed)


dataset = [
    [(4.4793, -4.075, -4.075), 0],
    [(-4.1793, -4.9218, 1.7664), 1],
    [(-3.9439, -0.7689, 4.8830), 1],
]


class Individual:
    def __init__(self, genotype):
        self.genotype = genotype
        self.W = (genotype[0:3])
        self.w = ((genotype[3:6]), (genotype[6:9]))
        self.w0 = (genotype[9:11])
        self.fitness = 0
    


class GenotypeSupplier:
    def __init__(self, size, start=0, end=1, seed=None):
        self.start = start
        self.end = end
        self.size = size
        if seed:
            random.seed(seed)

    def next(self):
        return [random.uniform(self.start, self.end) for i in range(0, self.size)]


def g(x):
    return math.e**x/(1+math.e**x)


def F(W, w, w0, E):
    return g(sum(
        W[j+1]*g(sum(
            w[j][k]*E[k]
            for k in range(0, 3)
        ) -w0[j])
        for j in range(0, 2)
    ) - W[0])


def E(W, w, w0):
    return sum((OUT - F(W, w, w0, IN))**2 for (IN,OUT) in dataset)


supplier = GenotypeSupplier(size=GENOTYPE_LEN,seed=RANDOM_SEED)
population = []
for i in range(0,P):
    population.append(Individual(supplier.next()))


for individual in population:
    individual.fitness = E(individual.W, individual.w, individual.w0)
    print("{:.2f}".format(individual.fitness))


