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
_breedings = {"simple_breed": breeds.simple_breed, "multiple_breed": breeds.multiple_breed,"uniform_breed":breeds.uniform_breed}

try:
    pickle_file = open("data.pickle", "rb")
    data = pickle.load(pickle_file)
    pickle_file.close()
except:
    data = {}

def run(b="simple_breed", ps="random", s="roulette", mutation=0.1, deviation=1, mutation_one_only=False, size=100, start=0, end=1, replacement=True, seed=0, Tc=0.1, To=10, k=0.0077, truncated=50,n=2,sc = "error", limit_fitness=100, max_generations=100000, max_error=0.0001):
    breed = _breedings[b]
    parent_selection = _selections[ps]
    selection = _selections[s]
    stop_condition = _stop_conditions[sc]

    parameters = (b, ps, s, mutation, deviation, mutation_one_only, size,start, end, replacement, seed, Tc, To, k,  truncated, n, sc, limit_fitness,max_generations,max_error)
    if not data.get(parameters)  :
        random.seed(seed)
        selections.Tc = Tc
        selections.To = To
        selections.k = k
        selections.TRUNC_N = truncated
        stops.limit_fitness = limit_fitness
        stops.max_error = max_error
        stops.max_generations = max_generations
        selections.t = 0
        breeds.n=n
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

def k_calculator(generation, percentage):
    return math.log(percentage)/(1 - generation)

#boltzmann tests
def boltzmann_tests():
    Tc = [0.1]
    To = [10]
    percentages = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    colors = [(1,x/10,0) for x in range(0,10,1)]
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


#Truncated Tests

def truncatedTests():
    K = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    colors = [(1,x/len(K),0) for x in range(0,len(K),1)]
    SIZE = 100
    for s in seeds[0:2]:
        plt.clf()
        plt.figure("Truncated comparison",figsize=(20,10))
        for k in K:
            print("running truncated with k = {}".format(k))
            generations = run(truncated=int(k*SIZE), s="truncated", sc="generation", max_generations=1000, seed=s, mutation=0.1, size=SIZE)
            generations = [ 1/x for x in generations]
            plt.plot(generations, label="k = {}".format(k), color=colors[K.index(k)])
                
        plt.legend()
        plt.xlabel("Generation")
        plt.ylabel("Error")
        plt.yscale("log")
        plt.title("Seed = {}".format(s))
        plt.savefig("truncated_comparison_{}.png".format(s))
    


#comparison of multipe_breed changes in N

def multiple_breed_tests():
    N = [2,3,4,5,6,7,8,9]
    colors = [(1,x/len(N),0) for x in range(0,len(N),1)]
    for s in seeds[0:2]:
        plt.clf()
        plt.figure("Multiple-breed comparison",figsize=(20,10))
        for n in N:
            print("running direct, multiple breed with N = {}".format(n))
            generations = run(s="direct", sc="generation", b="multiple_breed", n=n, max_generations=600, seed=s, mutation=0.1)
            generations = [ 1/x for x in generations]
            plt.plot(generations, label="n = {}".format(n), color=colors[N.index(n)])
                
        plt.legend()
        plt.title("Seed = {} selecting with elite/direct".format(s))
        plt.xlabel("Generation")
        plt.ylabel("Error")
        plt.yscale("log")
        plt.title("Seed = {}".format(s))
        plt.savefig("multiple_breed_comparison_{}.png".format(s))

#comparison of all algorithms with same parameters

def algorithmsTest(name,ls,lb,stop,max_gen=600,max_err=10**(-200), seeds =[seeds[0]], start=0, end=1, m=0.1, d=1, size=100):
    for seed in seeds:
        for key,s in ls.items():
            for bkey,b in lb.items():
                if key == "random":
                    continue
                print("running selection {}".format(key))
                generations = run(s=key,sc=stop,max_generations=max_gen,b=bkey,seed=seed,max_error=max_err, mutation=m, deviation=d, start=start, end=end, size=size)
                plt.figure("{} Fitness".format(name),figsize=(20,10))
                plt.yscale("log")
                plt.xlabel("Generations")
                plt.ylabel("Fitness")
                plt.plot(generations,label="{} {}".format(key, bkey))
                generations = [ 1/x for x in generations]

                plt.figure("{} Error".format(name),figsize=(20,10))
                plt.yscale("log")
                plt.xlabel("Generations")
                plt.ylabel("Error")
                plt.plot(generations, label="{} {}".format(key, bkey))


        plt.figure("{} Fitness".format(name),figsize=(20,10))
        plt.legend()
        plt.title("Seed = {}".format(seed))
        plt.savefig("{}_{}_fitness.png".format(name.replace(" ","_"),seed))
        plt.clf()
        plt.figure("{} Error".format(name),figsize=(20,10))
        plt.title("Seed = {}".format(seed))
        plt.legend()
        plt.savefig("{}_{}_error.png".format(name.replace(" ","_"),seed))
        plt.clf()
        #plt.show()



#mutation test

def mutationsTests(mutation_one_only=False):
    print("running mutation tests")
    probs = [0, 0.1, 0.5, 1]
    deviations = [1, 10, 50]
    for s in seeds[0:2]:
        plt.clf()
        plt.figure("mutation comparison" if not mutation_one_only else "mutation comparison only one",figsize=(20,10))
        for p in probs:
            for d in deviations:
                print("running mutation prob {} and deviation {}".format(p,d))
                generations = run(s="direct",sc="generation",max_generations=600, seed=s, mutation=p, deviation=d, mutation_one_only=mutation_one_only)
                generations = [ 1/x for x in generations]
                plt.plot(generations, label="p = {} d={}".format(p,d))
                    
            plt.legend()
            plt.title("Seed = {} selecting with elite/direct".format(s))
            plt.xlabel("Generation")
            plt.ylabel("Error")
            plt.yscale("log")
            plt.title("Seed = {}".format(s))
            if mutation_one_only:
                plt.savefig("mutation_one_comparison_{}.png".format(s))
            else:
                plt.savefig("mutation_comparison_{}.png".format(s))





if __name__ == "__main__":
    boltzmannTests()
    truncatedTests()
    multiple_breed_tests()
    mutationsTests()
    mutationsTests(True)
    algorithmsTest("All algorithms comparison Error simple breed 600 gens",_selections,{"simple_breed": breeds.simple_breed},"generation", max_gen=600)
    algorithmsTest("All algorithms comparison Error multiple breed 600 gens",_selections,{"multiple_breed": breeds.multiple_breed},"generation", max_gen=600)
    algorithmsTest("All algorithms comparison Error uniform breed 600 gens",_selections,{"uniform_breed": breeds.uniform_breed},"generation", max_gen=600)
    algorithmsTest({"direct": selections.direct},"multiple_breed","generation")
    algorithmsTest("Elite algorithms comparison Error breeding",{"direct": selections.direct},_breedings,"error")
    algorithmsTest("Roulette algorithms comparison Error breeding",{"roulette": selections.roulette},_breedings,"generation",max_gen=2000, seeds = seeds[0:3])
    algorithmsTest("Rank algorithms comparison Error breeding",{"rank": selections.rank},_breedings,"generation",max_gen=2000, seeds = seeds[0:3])
    algorithmsTest("Tournament algorithms comparison Error breeding",{"tournament": selections.tournament},_breedings,"generation",max_gen=2000, seeds = seeds[0:3])
    
    algorithmsTest("All algorithms extended range",_selections,{"simple_breed": breeds.simple_breed},"generation", max_gen=600, start=-10, end=10)
    algorithmsTest("All algorithms extended range high mutation",_selections,{"simple_breed": breeds.simple_breed},"generation", max_gen=200, start=-10, end=10, m=0.5, d=10)
    algorithmsTest("All algorithms high mutation",_selections,{"simple_breed": breeds.simple_breed},"generation", max_gen=200, m=0.5, d=10)
