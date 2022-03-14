import pickle
import rubik
from collections import deque


def search(root, ex):
    F = deque()
    F.append(root)
    ex[root] = rubik.manhattanDistancestate(root)
    while(F):
        node = F.popleft()
        for action in rubik.actions:
            state = action.action(node)
            if state not in ex:
                F.append(state)
                ex[state] = rubik.manhattanDistancestate(state)
    print('finished iterating')

ex = dict()
search(rubik.solved, ex)
filename = 'cornerDb'
outfile = open(filename,'wb')
pickle.dump(ex,outfile)
outfile.close()
print('termine')


#se levanta asi despues
#infile = open(filename,'rb')
#new_dict = pickle.load(infile)
#infile.close()