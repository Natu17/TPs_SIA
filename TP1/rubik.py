from collections import deque
from ntpath import join
import random

from search import Node

from algorithms import Bfs

solved = 'wwwwbbbboooogggrrryyy'
cubes = [[0,5,16], [1,14,15], [2,10,13], [3,6,9], [4,17,18],[7,8,19],[11,12,20]]
MAX_DEPTH = 9

class Action:
    def __init__(self, actionName, action):
        self.actionName = actionName
        self.action = action

#Front rotation
def F(state):
    return ''.join([state[17],state[1],state[2],state[16],
    state[7],state[4],state[5],state[6],
    state[3],state[0],state[10],state[11],
    state[12],state[13],state[14],
    state[15],state[18],state[19],
    state[8],state[9],state[20]])

# Front' rotation
def Fc(state):
    return ''.join([state[9],state[1],state[2],state[8],
    state[5],state[6],state[7],state[4],
    state[18],state[19],state[10],state[11],
    state[12],state[13],state[14],
    state[15],state[3],state[0],
    state[16],state[17],state[20]])

#Right rotation
def R(state):
    return ''.join([state[0],state[1],state[6],state[7],
    state[4],state[5],state[19],state[20],
    state[11],state[8],state[9],state[10],
    state[2],state[3],state[14],
    state[15],state[16],state[17],
    state[18],state[12],state[13]])


#Right' rotation
def Rc(state):
    return ''.join([state[0],state[1],state[12],state[13],
    state[4],state[5],state[2],state[3],
    state[9],state[10],state[11],state[8],
    state[19],state[20],state[14],
    state[15],state[16],state[17],
    state[18],state[6],state[7]])

#Top rotation
def T(state):
    return ''.join([state[3],state[0],state[1],state[2],
    state[4],state[9],state[10],state[7],
    state[8],state[13],state[14],state[11],
    state[12],state[15],state[16],
    state[5],state[6],state[17],
    state[18],state[19],state[20]])

#Top' rotation
def Tc(state):
    return ''.join([state[1],state[2],state[3],state[0],
    state[4],state[15],state[16],state[7],
    state[8],state[5],state[6],state[11],
    state[12],state[9],state[10],
    state[13],state[14],state[17],
    state[18],state[19],state[20]])


actions = [Action('F',F),Action('F\'',Fc),Action('R',R),Action('R\'',Rc),Action('T',T),Action('T\'',Tc)]

def check(state):
    return state == solved


#scrumble for starting position
def scramble():
    #return("gobybwbyorowgwbyrwygo","SAMPLE BFS") #depth 10
    return("gwoyowbogrbgoyrbrwbyw", "SAMPLE BFS") #depth 14
    #return("gowwoyryrbgobrgwobybw", "SAMPLE BFS") #depth 12
    #return("wgrgyowrwowrbgoybobby", "SAMPLE DFS") 
    #return("bbrwywowbgywrbyoogorg", "SAMPLE DFS") 
    #return("bgwyorgoyoorbgrwwwbby", "SAMPLE DFSVL")
    # bbrwywowbgywrbyoogorg
    state = solved
    moves = ''
    rand = 0
    for i in range(MAX_DEPTH):
        rand = random.randint(0,len(actions)-1)
        state = actions[rand].action(state)
        moves += actions[rand].actionName + ' '
    return (state, moves)




def heurManDist(node):
    heuristic = 0
    for i in cubes:
        heuristic += manhBfs(node, i)
    return heuristic/4

def cubeCheck(state, cube):
    a = True
    for i in cube:
        if state[i] != solved[i]:
            a = False
            return a
    return a

def manhBfs(root, cube):
    F = deque()
    ex = dict()
    F.append(root)
    ex[root.state] = 1
    while F:
        node = F.popleft()
        state = node.state
        for action in actions:
            state = action.action(node.state)
            if not(state in ex): #Create Node AFTER state not explored check
                child = Node(state, node, action.actionName, node.depth + 1)
                if cubeCheck(state, cube):
                    return child.depth
                F.append(child)
    return


import time

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