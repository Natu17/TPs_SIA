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

def set_winner(competitor1,competitor2):
    print(competitor1)
    print(competitor2)
    u = random.uniform(0.5,1)
    print(u)
    r = random.uniform(0,1)
    print("r:")
    print(r)
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


    

    

