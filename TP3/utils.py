import numpy as np
import random



def noise(number, probability=0.2, seed=0):
    if seed:
        random.seed(seed)
    to_ret = np.zeros(len(number))
    for i in range(0, len(number)):
        if random.random() < probability:
            to_ret[i] = 1-number[i]
        else: 
            to_ret[i] = number[i]
    return to_ret