import time
from rubik import *
def get_moves(pos):
	return [F(pos),Fc(pos),R(pos),Rc(pos),T(pos),Tc(pos)]
def depth():
    start_time = time.time()
    dist = [{solved}, set(get_moves(solved))]
    while dist[-1]:
        dist.append(set())
        for pos in dist[-2]:
            for sub_pos in get_moves(pos):
                if sub_pos not in dist[-2] and sub_pos not in dist[-3]:
                    dist[-1].add(sub_pos)
        print('Depth ' + str(len(dist) - 1) + ': ' + str(len(dist[-1])) + ' positions')
    print('2x2 Depth is ' + str(len(dist) - 2) + ', solved in ' + str(round(time.time() - start_time, 2)) + ' seconds')
    return dist
d = depth()

for i in range(1,len(d)):
    print("depth " + str(i) + ":")
    print(random.sample(d[i],5 if len(d[i])>5 else len(d[i])))
    print("")