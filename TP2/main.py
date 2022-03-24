import math
import random
from genetic_algorithm import GeneticAlgorithm
import argparse
import selections
import breeds
import sys
import json
import time
import matplotlib.pyplot as plt
import os

config_path = sys.argv[1] if len(sys.argv)>1 else "config.json"

try:
    file = open(config_path)
    config = json.load(file)
except FileNotFoundError:
    print("config not found")
    config = {}
config.setdefault("population",500)
config.setdefault("seed", 0)
config.setdefault("mutation",0.01)
config.setdefault("deviation",1)
config.setdefault("parents_selection","roulette")
config.setdefault("selection","direct")
config.setdefault("breeding","simple_breed")
config.setdefault("N",10)
config.setdefault("error",0.0001)

GENOTYPE_LEN = 11
P = config.get("population")
RANDOM_SEED = config.get("seed")
MUTATION_PROBABILITY = config.get("mutation")
MUTATION_DEVIATION = config.get("deviation")

breedings = {"simple_breed":breeds.simple_breed, "multiple_breed": lambda p1,p2: breeds.multiple_breed(p1,p2,config.get("N"))}
selections = {"roulette":selections.roulette, "direct":selections.direct}

breeding_function = breedings[config.get("breeding")]
parent_selection_function = selections[config.get("parents_selection")]
selection_function = selections[config.get("selection")]

if not RANDOM_SEED: RANDOM_SEED = time.time_ns()
random.seed(RANDOM_SEED)

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



def stop_condition(generations):
    return generations[-1].fitness > 1/config.get("error")

algorithm = GeneticAlgorithm(fitness, breeding_function, parent_selection_function, selection_function, GENOTYPE_LEN, MUTATION_PROBABILITY, MUTATION_DEVIATION, P)

#plt.ion()
plt.figure("error graph")
while True:
    generations = algorithm.next()
    if stop_condition(generations):
        break
    
    plt.clf()
    plt.title("error graph")
    plt.gca().set_xlabel("generations")
    plt.gca().set_ylabel("error")
    plt.grid()
    #if len(generations)<40:
    plt.plot([i for i in range(0,len(generations))], [1/generation.fitness for generation in generations])
    ##else:
    #plt.plot([i for i in range(len(generations)-40,len(generations))], [1/generation.fitness for generation in generations[-40:]])

    plt.pause(0.01)

#plt.ioff()
plt.draw()

path = "./results/{}/".format(RANDOM_SEED)
os.makedirs(path, exist_ok=True)

with open(path + "config.json", "w") as f:
    config["seed"] = RANDOM_SEED
    json.dump(config, f, indent=4)
with open(path+"output.json", "w") as f:
    best = generations[-1].population[0].genotype
    W = best[0:3]
    w = ((best[3:6]), (best[6:9]))
    w0 = (best[9:11])
    info = {"generations":len(generations),"individual":{"W": W, "w": w, "w0": w0}, "F1": F(W, w, w0, dataset[0][0]), "F2": F(W, w, w0, dataset[1][0]), "F3": F(W, w, w0, dataset[2][0]), "E": E(W, w, w0)}
    json.dump(info, f, indent=4)
    plt.savefig(path+"error_graph.png")