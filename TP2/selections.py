import random

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