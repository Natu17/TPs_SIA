from collections import deque

from numpy import empty
from graphics import update
from sortedcontainers import sortedlist

graphics = False

class Node:
    def __init__(self, state,parent = None, action = None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

class HeuristicNode:
    def __init__(self, state,parent = None, action = None, depth=0, heuristic = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.heuristic = heuristic

class Dfs:
    def __init__(self):
        self.F = deque()
        self.ex = dict()
    
    def add(self,child):
        self.F.append(child)
        self.ex[child.state] = 1
    
    def pick(self):
        return self.F.pop()

    def isEmpty(self):
        return not(self.F)

    def needExploring(self, state, depth):
        return not(state in self.ex)

class Bfs:
    def __init__(self):
        self.F = deque()
        self.ex = dict()
    
    def add(self,child):
        self.F.append(child)
        self.ex[child.state] = 1
    
    def pick(self):
        return self.F.popleft()
    
    def isEmpty(self):
        return not(self.F)

    def needExploring(self, state, depth):
        return not(state in self.ex)

class Dfsvl:
    
    def __init__(self, limit, step):
        self.limit = limit
        self.step = step
        self.F1 = deque()
        self.F2 = deque()
        self.ex = dict()

    def add(self,child):
        if child.depth > self.limit:
            self.F2.append(child)
        else: self.F1.append(child)
        self.ex[child.state] = child.depth
    
    def pick(self):
        if not(self.F1): 
            F = self.F1
            self.F1 = self.F2
            self.F2 = F
            self.limit += self.step
        return self.F1.pop()

    def isEmpty(self):
        return not(self.F1 or self.F2)

    def needExploring(self, state, depth):
        d = self.ex.get(state)
        return d is None or d < depth

      
    


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


def localHeuristicSearch(root, actions, condition):
    r = HeuristicNode(root)
    F = deque()
    ex = dict()
    l = sortedlist()
    F.append(r)
    ex[root] = 1
    while not(F.isEmpty()):
        node = F.pop
        state = node.state
        for action in actions:
            state = action.action(node.state)
            if state not in ex: #Create Node AFTER state not explored check
                child = HeuristicNode(state, node, action.actionName, node.depth + 1)
                if condition(state):
                    moves = ''
                    while(child):
                        if(child.action): moves = ' '.join([child.action,moves])
                        child = child.parent
                    return moves
                l.add(child)
                if graphics: update(child)
                while l is not empty:
                    F.append(l.pop())
    print('solution not found')


dfs = lambda root,actions,condition: search(root,actions,condition, Dfs() )
bfs = lambda root,actions,condition: search(root,actions,condition,Bfs())
dfsvl = lambda root, actions, condition, limit, step: search(root,actions, condition, Dfsvl(limit,step))
