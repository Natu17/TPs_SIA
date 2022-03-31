import math
import random
import genetic_algorithm 
import functions
import selections
import breeds
import sys
import json
import time
import matplotlib.pyplot as plt
import os
import stops

config_path = sys.argv[1] if len(sys.argv) > 1 else "config.json"

try:
    file = open(config_path)
    config = json.load(file)
except FileNotFoundError:
    print("config not found")
    config = {}
config.setdefault("population", 500)
config.setdefault("seed", 0)
config.setdefault("mutation", 0.01)
config.setdefault("mutation_one", False)
config.setdefault("deviation", 1)
config.setdefault("parents_selection", "roulette")
config.setdefault("selection", "direct")
config.setdefault("breeding", "simple_breed")
config.setdefault("N", 10)
config.setdefault("error", 0.0001)
config.setdefault("max_generations", 100000)
config.setdefault("To", 100)
config.setdefault("Tc", 1)
config.setdefault("k", 0.01)
config.setdefault("TRUNC_N", 10)
config.setdefault("range", [0, 1])
config.setdefault("stop_condition","error")
config.setdefault("parents_replacement",True)
config.setdefault("limit_fitness",100)

GENOTYPE_LEN = 11
P = config.get("population")
RANDOM_SEED = config.get("seed")
MUTATION_PROBABILITY = config.get("mutation")
MUTATION_ONE = config.get("mutations")
MUTATION_DEVIATION = config.get("deviation")

_breedings = {"simple_breed": breeds.simple_breed, "multiple_breed": lambda p1,
              p2: breeds.multiple_breed(p1, p2, config.get("N"))}
_selections = {"roulette": selections.roulette, "direct": selections.direct, "rank": selections.rank,
               "tournament": selections.tournament, "truncated": selections.truncated, "boltzmann": selections.boltzmann}
_stop_conditions = {"error":stops.error_stop, "generation":stops.generation_stop,"fitness":stops.fitness_stop}


breeding_function = _breedings[config.get("breeding")]
parent_selection_function = _selections[config.get("parents_selection")]
selection_function = _selections[config.get("selection")]
stop_condition = _stop_conditions[config.get("stop_condition")]


stops.limit_fitness = config.get("limit_fitness")
stops.max_error = 10**(-config.get("error"))
stops.max_generations = config.get("max_generations")
population_range = config.get("range")

selections.To = config.get("To")
selections.Tc = config.get("Tc")
selections.k = config.get("k")

selections.TRUNC_N = config.get("TRUNC_N")


if not RANDOM_SEED:
    RANDOM_SEED = time.time_ns()
random.seed(RANDOM_SEED)


def main():

    algorithm = genetic_algorithm.GeneticAlgorithm(functions.fitness, breeding_function, parent_selection_function,
                                 selection_function, GENOTYPE_LEN, MUTATION_PROBABILITY, MUTATION_DEVIATION,MUTATION_ONE, P, population_range[0], population_range[1],config.get("parents_replacement"))

    # plt.ion()
    plt.figure("error graph")
    start = (time.time(), time.process_time())
    while True:
        generations = algorithm.next()
        selections.t += 1
        if stop_condition(generations):
            break

        plt.clf()
        plt.title("error graph")
        plt.gca().set_xlabel("generations")
        plt.gca().set_ylabel("error")
        plt.grid()
        if len(generations) < 40:
            plt.plot([i for i in range(0, len(generations))], [
                functions.error(generation.genotype) for generation in generations])
        else:
            plt.plot([i for i in range(len(generations)-40, len(generations))],
                     [functions.error(generation.genotype) for generation in generations[-40:]])

        plt.pause(0.01)

    end = (time.time(), time.process_time())

    print("wall time:", end[0]-start[0], "\ncpu time:", end[1]-start[1])

    # plt.ioff()
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
        info = {"generations": len(generations), "individual": {"W": W, "w": w, "w0": w0}, "F1": functions.F(
            W, w, w0, functions.dataset[0][0]), "F2": functions.F(W, w, w0, functions.dataset[1][0]), "F3": functions.F(W, w, w0, functions.dataset[2][0]), "E": functions.E(W, w, w0)}
        json.dump(info, f, indent=4)
        plt.savefig(path+"error_graph.png")


if __name__ == "__main__":
    main()
