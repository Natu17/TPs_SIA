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

iterations = 10
SEED = 2023
random.seed(SEED)
seeds = [random.randint(0, 2**16) for i in range(iterations)]
_selections = {"roulette": selections.roulette, "direct": selections.direct, "rank": selections.rank,
               "tournament": selections.tournament, "truncated": selections.truncated, "boltzmann": selections.boltzmann, "random": selections.random_selec}
_stop_conditions = {"error": stops.error_stop,
                    "generation": stops.generation_stop, "fitness": stops.fitness_stop}
_breedings = {"simple_breed": breeds.simple_breed, "multiple_breed": lambda p1,
              p2: breeds.multiple_breed(p1, p2, 2)}

try:
    pickle_file = open("data.pickle", "rb")
    data = pickle.load(pickle_file)
    pickle_file.close()
except:
    data = {}

def run(b="simple_breed", ps="random", s="roulette", mutation=0.1, deviation=1, mutation_one_only=False, size=100, start=0, end=1, replacement=True, seed=0, Tc=0.1, To=10, k=0.0077, truncated=20,sc = "error", limit_fitness=100, max_generations=100000, max_error=0.0001):
    breed = _breedings[b]
    parent_selection = _selections[ps]
    selection = _selections[s]
    stop_condition = _stop_conditions[sc]

    parameters = (b, ps, s, mutation, deviation, mutation_one_only, size,start, end, replacement, seed, Tc, To, k,  truncated, sc, limit_fitness,max_generations,max_error)
    if not data.get(parameters)  :
        random.seed(seed)
        selections.Tc = Tc
        selections.To = To
        selections.k = k
        selections.truncated = truncated
        stops.limit_fitness = limit_fitness
        stops.max_error = max_error
        stops.max_generations = max_generations
        selections.t = 0
        algorithm = genetic_algorithm.GeneticAlgorithm(
            functions.fitness, breed, parent_selection, selection, GENOTYPE_LEN, mutation, deviation, mutation_one_only, size, start, end, replacement)
        while True:
            generations = algorithm.next()
            selections.t += 1
            if stop_condition(generations):
                data[parameters] = [x.fitness for x in generations]
                with open("data.pickle", "wb") as f:
                    try:
                        pickle.dump(data, f)
                    except:
                        pass
                    f.close()
                return [x.fitness for x in generations]
    else:
        return data[parameters]


#boltzmann tests

Tc = [0.1]
To = [10]
percentages = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
colors = [(1,x/10,0) for x in range(0,10,1)]
def k_calculator(generation, percentage):
    return math.log(percentage)/(1 - generation)

def boltzmann_tests():
    for m in [0.001, 0.1]:
        for s in seeds[0:2]:
            plt.clf()
            plt.figure("Boltzmann comparison",figsize=(20,10))
            for tc in Tc:
                for to in To:
                    for percentage in percentages:
                        k = k_calculator(300, percentage)
                        print("running boltzmann with Tc = {}, To = {}, k = {} , p = {}".format(tc, to, k, percentage))
                        generations = run(Tc=tc, To=to, k=k, s="boltzmann", sc="generation", max_generations=1000, seed=s, mutation=m)
                        generations = [ 1/x for x in generations]
                        plt.plot(generations, label="Tc = {}, To = {}, k = {}, p = {}".format(tc, to, k, percentage), color=colors[percentages.index(percentage)])
                        
            plt.legend()
            plt.xlabel("Generation")
            plt.ylabel("Error")
            plt.yscale("log")
            plt.title("Seed = {}".format(s))
            plt.savefig("boltzmann_comparison_{}_mutation_{}.png".format(s,m))
            #plt.show()


#comparison of all algorithms with same parameters

def algorithmsTest600():
    
    for key,s in _selections.items():
        if key == "random":
            continue
        print("running selection {}".format(key))
        generations = run(s=key, sc="generation", max_generations=600, seed=seeds[0])

        plt.figure("All algorithms comparison Fitness",figsize=(20,10))
        plt.yscale("log")
        plt.xlabel("Generations")
        plt.ylabel("Fitness")
        plt.plot(generations, label=key)
        generations = [ 1/x for x in generations]
        
        plt.figure("All algorithms comparison Error",figsize=(20,10))
        plt.yscale("log")
        plt.xlabel("Generations")
        plt.ylabel("Error")
        plt.plot(generations, label=key)


    plt.figure("All algorithms comparison Error",figsize=(20,10))
    plt.legend()
    plt.savefig("all_algorithms_comparison_error_600.png")
    plt.figure("All algorithms comparison Fitness",figsize=(20,10))
    plt.legend()
    plt.savefig("all_algorithms_comparison_fitness_600.png")
    #plt.show()





if __name__ == "__main__":
    algorithmsTest600()


   
exit(1)

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
                stops.max_generations = _generations
                generations = run(breeds.simple_breed,
                                  selections.boltzmann, 0.1, 1, 10, seed, tc, to, k, 1)
                end = time.time()
                print("{} fitness in {:.2f} secs".format(
                    generations[0], end-start))
                boltzmann[(tc, to, p)].append(generations)


errors = []
fitnesses = []
plt.figure("boltzmann")
for p in percentages:
    f = boltzmann[(0.1, 20, p,)]
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
