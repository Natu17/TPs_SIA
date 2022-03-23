from audioop import reverse
import random
from sortedcontainers import SortedList

def simpleBreeds(genotype1,genotype2):
    p = random.randint(0, len(genotype1))
    genotypeFinal = genotype1[0:p] + genotype2[p:len(genotype2)]
    return genotypeFinal








