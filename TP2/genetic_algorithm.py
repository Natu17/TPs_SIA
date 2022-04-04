import random
from sortedcontainers import SortedList
from dataclasses import dataclass


@dataclass
class Individual:
    genotype: list
    fitness: float = 0



class GenotypeSupplier:
    def __init__(self, size, start=0, end=1):
        self.start = start
        self.end = end
        self.size = size

    def next(self):
        return [random.uniform(self.start, self.end) for i in range(0, self.size)]

class Generation:
    def __init__(self):
        self.population = SortedList(key=lambda individual : -individual.fitness)
        self.fitness = 0

    def add(self, individual):
        self.population.add(individual)
        if individual.fitness > self.fitness:
            self.fitness = individual.fitness
            self.genotype = individual.genotype
    

@dataclass
class GeneticAlgorithm:
    fitness_fuction: any
    breeding_function: any
    parent_selection_function: any
    selection_function: any
    genotype_len: int
    mutation_probability: float = 0.01
    mutation_deviation: float = 0
    mutation_one_only: bool = False
    population_size: int = 100
    range_start: float = 0
    range_end: float = 1
    parents_replacement: bool = True

    
    def __post_init__(self):
        self.generations = []


    def create_initial_generation(self):
        supplier = GenotypeSupplier(size=self.genotype_len, start = self.range_start, end=self.range_end)
        generation = Generation()
        for i in range(0, self.population_size):
            genotype = supplier.next()
            generation.add(Individual(genotype, self.fitness_fuction(genotype)))
        return generation

    def mutation(self,genotype):
        for idx,gen in enumerate(genotype):
            if random.random() < self.mutation_probability:
                genotype[idx] += random.gauss(0,self.mutation_deviation)
        return genotype

    def mutation_one(self,genotype):
        idx = random.randint(0,len(genotype)-1)
        if random.random() < self.mutation_probability:
            genotype[idx] += random.gauss(0,self.mutation_deviation)
        return genotype
    
    def generate_children(self,generation):
        children = []
        parents = generation.population.copy()
        while len(children) < self.population_size:
            parent1 = self.parent_selection_function(parents)
            if not self.parents_replacement:
                parents.remove(parent1)
            parent2 = self.parent_selection_function(parents)
            if not self.parents_replacement:
                parents.remove(parent2)

            childs = self.breeding_function(parent1.genotype,parent2.genotype)
            for child in childs:
                if self.mutation_one_only: 
                    genotype = self.mutation_one(child)
                else: 
                    genotype = self.mutation(child)
                children.append(Individual(genotype,self.fitness_fuction(genotype)))
        return children

    def next(self):
        if not self.generations:
            initial_generation = self.create_initial_generation()
            self.generations = [initial_generation]

        
        children = self.generate_children(self.generations[-1])

        candidates = sorted(children + self.generations[-1].population, key=lambda i: -i.fitness)
        new_generation = Generation()

        for i in range(0,self.population_size):
            selected = self.selection_function(candidates)
            candidates.remove(selected)
            new_generation.add(selected)
        
        self.generations.append(new_generation)

        return self.generations
            
            



