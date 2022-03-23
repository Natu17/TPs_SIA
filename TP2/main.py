import math
import population
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


def fitness(genotype):
    W = (genotype[0:3])
    w = ((genotype[3:6]), (genotype[6:9]))
    w0 = (genotype[9:11])
    return 1/E(W, w, w0)



def mutation(child):
    return child

def selection(population):
    return population[0]

def breed(parent1, parent2):
    return (parent1.genotype,parent2.genotype)

def stop_condition(generations):
    return len(generations) > 100

population.run(P, GENOTYPE_LEN, RANDOM_SEED, fitness, mutation, selection, breed, stop_condition)