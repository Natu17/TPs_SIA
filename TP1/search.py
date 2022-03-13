from graphics import update
from algorithms import *

graphics = True

class Node:
    def __init__(self, state,parent = None, action = None, depth=0, heuristic = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.heuristic = heuristic

def search(root, actions, condition, manager):
    r=Node(root)
    manager.add(r)
    while not(manager.isEmpty()):
        node = manager.pick()
        state = node.state
        for action in actions:
            state = action.action(node.state)
            if manager.needExploring(state, node.depth + 1): #Create Node AFTER state not explored check
                child = Node(state, node, action.actionName, node.depth + 1)
                if condition(state):
                    moves = ''
                    while(child):
                        if(child.action): moves = ' '.join([child.action,moves])
                        child = child.parent
                    return moves
                manager.add(child)
                if graphics: update(child)
    print('solution not found')


dfs = lambda root,actions,condition: search(root,actions,condition, Dfs() )
bfs = lambda root,actions,condition: search(root,actions,condition,Bfs())
dfsvl = lambda root, actions, condition, limit, step: search(root,actions, condition, Dfsvl(limit,step))
localHeuristic = lambda root,actions,condition, heuristic: search(root,actions,condition, LocalHeuristic(heuristic))
globalHeuristic = lambda root,actions,condition, heuristic: search(root,actions,condition, GlobalHeuristic(heuristic))
a = lambda root,actions,condition, heuristic: search(root,actions,condition, GlobalHeuristic(lambda node : node.depth + heuristic(node)))
