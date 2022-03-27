import random, math

def direct(candidates):
    return candidates[0]


def roulette_base(scores):
    total_probability = sum(scores)
    result = random.uniform(0,total_probability)
    total_probability = 0
    for i, score in enumerate(scores):
        total_probability += score
        if total_probability >= result:
            return i
    return -1

def roulette(candidates):
    
    index = roulette_base([c.fitness for c in candidates])
    return candidates[index]

def rank(candidates):
    l = len(candidates)
    total_probability = l* (l + 1) / 2
    result = random.randint(0,total_probability)
    total_probability = 0
    for i in range(0,l):
        total_probability += l-i
        if total_probability >= result:
            return candidates[i]
    return -1 #error


def set_winner(competitor1,competitor2):
    u = random.uniform(0.5,1)
    r = random.uniform(0,1)
    if r < u:
        if competitor1.fitness < competitor2.fitness : competitor1 = competitor2
    else:
         if competitor2.fitness < competitor1.fitness : competitor1 = competitor2 
    return competitor1 


def tournament(candidates):
    list_couples = random.sample(candidates, 4)#diferents couples always?
    competitor1 = set_winner(list_couples[0],list_couples[1])
    competitor2 = set_winner(list_couples[2],list_couples[3])
    winner = set_winner(competitor1,competitor2)
    return winner

def truncated(candidates,n):
    if n < len(candidates):
        winner = random.choice(candidates[0:len(candidates) - n])
        return winner
    else:
        return -1 #error


Tc =0.5
To = 1
t = 0
k=1

def temperature():
    return Tc + (To - Tc)*math.exp(-k*t)

def boltzmann(candidates):
    
    T = temperature()

    scores = [math.exp(c.fitness/T) for c in candidates]

    return candidates[roulette_base(scores)]
