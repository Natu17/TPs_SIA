import selections
import genetic_algorithm
import breeds
import functions
import random
import math
import stops
import time
import statistics
import matplotlib.pyplot as plt
import numpy as np
import pickle

GENOTYPE_LEN = 11

iterations = 50
seed = 2022
random.seed(seed)
seeds = [random.randint(0, 2**16) for i in range(iterations)]


_selections = [selections.direct, selections.roulette, selections.rank,
               selections.tournament]
#_selections_info = [{name:"direct"}, {name:"roulette"}, {name: "rank"}, {name:"tournament"}]
_breedings = [breeds.simple_breed, breeds.multiple_breed, breeds.uniform_breed]
generations = [500]
populations = [10, 100, 500]
mutations = [0.01, 0.1, 0.5]
deviations = [1, 5, 10]
Tc = [0.1, 0.5, 1]
To = [20, 10, 5]
percentages = [0.1, 0.3, 0.5]
truncated = [0.9, 0.75, 0.5]  # in 500 generations


def k_calculator(generation, percentage):
    return math.log(percentage)/(1 - generation)


try:
    pickle_file = open("data.pickle", "rb")
    data = pickle.load(pickle_file)
    pickle_file.close()
except:
    data = {}


def run(breed, selection, mutation, deviation, size, seed, Tc, To, k, truncated):
    if not data.get((breed, selection, mutation, deviation, size,seed ,Tc, To, truncated, k)):
        random.seed(seed)
        selections.Tc = tc
        selections.To = to
        selections.k = k
        selections.truncated = truncated
        algorithm = genetic_algorithm.GeneticAlgorithm(
            functions.fitness, breed, selections.roulette, selection, GENOTYPE_LEN, mutation, deviation, size, 0, 1)
        while True:
            generations = algorithm.next()
            selections.t += 1
            if stops.generation_stop(generations):
                data[(breed, selection, mutation, deviation, size,seed, Tc, To, truncated, k)] = [x.fitness for x in generations]
                with open("data.pickle", "wb") as f:
                    pickle.dump(data, f)
                    f.close()
                return [x.fitness for x in generations]
    else:
        return data[(breed, selection, mutation, deviation, size, seed, Tc, To, truncated, k)]


# Boltzmann tests
_generations = 500
boltzmann = {}
for tc in Tc:
    for to in To:
        for p in percentages:
            boltzmann[(tc, to, p)] = []
            for seed in seeds:
                random.seed(seed)
                k = k_calculator(_generations, p)
                print("running boltzmann with Tc = {}, To = {}, k = {}, p = {}".format(
                    tc, to, k, p))
                start = time.time()
                generations = run(breeds.simple_breed,
                                  selections.boltzmann, 0.1, 1, 10, seed,tc,to,k,1)
                end = time.time()
                print("{} fitness in {:.2f} secs".format(
                    generations[-1], end-start))
                boltzmann[(tc, to, p)].append(generations)


errors = []
fitnesses = []
plt.figure("boltzmann")
for p in percentages:
    f = boltzmann[(0.1,20, p,)]
    #f = np.transpose(f)
    fitnesses = np.mean(f, axis=0)
    #errors = np.std(f, axis=0)
    # fitnesses.append(f)
    # errors.append(statistics.stdev(f)/math.sqrt(len(f)))
    plt.plot(fitnesses)
plt.show()
exit(1)
for selection in _selections:
    for breed in _breedings:
        for gen in generations:
            for mutation in mutations:
                for deviation in deviations:
                    for size in populations:
                        for seed in seeds:
                            random.seed(seed)
                            stops.max_generations = gen
                            print("running with selection")
                            generations = run(
                                breed, selection, mutation, deviation, size, seed)
