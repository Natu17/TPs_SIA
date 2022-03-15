import pickle
import rubik
import heuristics
from collections import deque



filename = 'cornerDb'
#se levanta asi despues
infile = open(filename,'rb')
new_dict = pickle.load(infile)
print('file loaded')
infile.close()

def manhattanwithdict(node):
    return new_dict[node.state]