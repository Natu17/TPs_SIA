import random

class Individual:
    def __init__(self, genotype, fitness):
        self.genotype = genotype
        self.fitness = fitness
    


class GenotypeSupplier:
    def __init__(self, size, start=0, end=1, seed=None):
        self.start = start
        self.end = end
        self.size = size
        if seed:
            random.seed(seed)

    def next(self):
        return [random.uniform(self.start, self.end) for i in range(0, self.size)]





def children_generation(generation, fitness, breed, selection, mutation):
    children = []
    while len(children) < len(generation):
        parent1 = selection(generation)
        parent2 = selection(generation)
        childs = breed(parent1,parent2)
        for child in childs:
            genotype = mutation(child)
            children.append(Individual(genotype,fitness(genotype)))

    return children

def create_population(fitness, population_size ,genotype_len, random_seed):
    supplier = GenotypeSupplier(size=genotype_len, seed=random_seed)
    population = []
    for i in range(0, population_size):
        genotype = supplier.next()
        population.append(Individual(genotype, fitness(genotype)))
    return population



def sort(population):
    return sorted(population, key= lambda individual: -individual.fitness)

def run(population_size, genotype_len, random_seed, fitness, mutation, selection, breed, stop_condition):
    initial_population = create_population(fitness, population_size, genotype_len,random_seed)
    generations = [sort(initial_population)]

    while not stop_condition(generations):
        children = children_generation(generations[-1],fitness, breed,selection,mutation)

        candidates = sort(children + generations[-1])
        new_generation = []

        for i in range(0,population_size):
            selected = selection(candidates)
            candidates.remove(selected)
            new_generation.append(selected)
        
        generations.append(sort(new_generation))
        
        

