import functions

max_error = 10**(-200)

max_generations = 500

limit_fitness = 100

def error_stop(generations):
    return functions.error(generations[-1].population[0].genotype) < max_error

def generation_stop(generations):
    return len(generations) >= max_generations

def fitness_stop(generations):
    for i in range (1, limit_fitness + 1):
        if generations[-i].fitness != generations[-i-1].fitness:
            return False
    return True