import random

random.seed(17)

def noise(number):
    for i in range(0, len(number)):
        if random.rand() < 0.2:
            number[i] = 1-number[i]