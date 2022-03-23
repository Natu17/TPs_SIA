from functools import reduce
import random
from main import fitness
from population import create_population


def direct(candidates):
    return candidates[0]


def roulette(candidates):
    total_probability = sum(candidate.fitness for candidate in candidates)
    result = random.uniform(0,total_probability)
    total_probability = 0

    for i in candidates:
        total_probability += i.fitness
        if total_probability >= result:
            return i
    return