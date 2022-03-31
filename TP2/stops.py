import functions

max_error = 10**(-2)

max_generations = 500

def error_stop(generations):
    return functions.error(generations[-1].population[0].genotype) < max_error

def generation_stop(generation):
    return len(generations) >= max_generations
