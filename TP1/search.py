from graphics import update
from algorithms import *

graphics = False

class Node:
    def __init__(self, state,parent = None, action = '', depth=0, heuristic = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.heuristic = heuristic

def search(root, actions, condition, manager,noGraphics=False):
    r=Node(root)
    if condition(root):
        return {"nodes":[r], "border":0, "explored":0, "depth":0}
    manager.add(r)
    while not(manager.isEmpty()):
        node = manager.pick()
        state = node.state
        for action in actions:
            state = action.action(node.state)
            if manager.needExploring(state, node.depth + 1): #Create Node AFTER state not explored check
                child = Node(state, node, action.actionName, node.depth + 1)
                if condition(state):
                    #moves = ''
                    list = deque()
                    depth = child.depth
                    while(child):
                        #if(child.action): moves = ' '.join([child.action,moves])
                        list.appendleft(child)
                        child = child.parent
                    return {"nodes":list, "border":manager.getBorder(), "explored":manager.getExplored(), "depth":depth}
                manager.add(child)
                if not(noGraphics) and graphics: update(child)
    print('solution not found')


dfs = lambda root,actions,condition: search(root,actions,condition, Dfs() )
bfs = lambda root,actions,condition, noGraphics=False: search(root,actions,condition,Bfs(), noGraphics)
dfsvl = lambda root, actions, condition, limit, step: search(root,actions, condition, Dfsvl(limit,step))
localHeuristic = lambda root,actions,condition, heuristic: search(root,actions,condition, LocalHeuristic(heuristic))
globalHeuristic = lambda root,actions,condition, heuristic: search(root,actions,condition, GlobalHeuristic(heuristic))
a = lambda root,actions,condition, heuristic: search(root,actions,condition, GlobalHeuristic(lambda node : node.depth + heuristic(node)))
