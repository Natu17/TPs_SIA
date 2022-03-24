from audioop import reverse
import random
from sortedcontainers import SortedList

def simple_breed(genotype1,genotype2):
    p = random.randint(0, len(genotype1))
    genotypeFinal1 = genotype1[0:p] + genotype2[p:len(genotype2)]
    genotypeFinal2 = genotype2[0:p] + genotype1[p:len(genotype1)]
    return (genotypeFinal1, genotypeFinal2)

def multiple_breed(genotype1,genotype2,n):
    if n < len(genotype1): 
        points = SortedList()
        l = [ i for i in range(1,len(genotype1))]
        while len(points) < n:
            p = random.choice(l)
            l.remove(p)
            points.add(p)
        points.add(len(genotype1))
        p1 = 0
        genotypes = [[],[]]
        while  len(points) > 0:
            p2 = points.pop(0)
            genotypes[0] += genotype1[p1:p2] 
            genotypes[1] += genotype2[p1:p2]
            aux = genotypes[0]
            genotypes[0] = genotypes[1]
            genotypes[1] = aux
            p1 = p2

    return genotypes