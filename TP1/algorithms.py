from collections import deque
from sortedcontainers import SortedList


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

    def getExplored(self):
        return len(self.ex) - self.getBorder()
    
    def getBorder(self):
        return len(self.F)

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
    
    def getExplored(self):
        return len(self.ex) - self.getBorder()
    
    def getBorder(self):
        return len(self.F)

class Dfsvl:
    
    def __init__(self, limit, step):
        self.limit = limit
        self.step = step
        self.F1 = deque()
        self.F2 = deque()
        self.ex = dict()
        self.explored = 0

    def add(self,child):
        if child.depth > self.limit:
            self.F2.append(child)
        else: self.F1.append(child)
        self.ex[child.state] = child.depth
    
    def pick(self):
        self.explored+=1
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

    def getExplored(self):
        return self.explored
    
    def getBorder(self):
        return len(self.F1) + len(self.F2)

class LocalHeuristic:
    def __init__(self, heuristic):
        self.F = deque()
        self.ex = dict()
        self.l = SortedList(key=lambda node: node.heuristic)
        self.heuristic = heuristic
    
    def add(self,child):
        child.heuristic = self.heuristic(child)
        self.l.add(child)
        self.ex[child.state] = 1
    
    def pick(self):
        while self.l:
            self.F.append(self.l.pop())
        return self.F.pop()

    def isEmpty(self):
        return not(self.F or self.l)

    def needExploring(self, state, depth):
        return not(state in self.ex)
    
    def getExplored(self):
        return len(self.ex) - self.getBorder()
    
    def getBorder(self):
        return len(self.F) + len(self.l)

class GlobalHeuristic:
    def __init__(self, heuristic):
        self.F = SortedList(key=lambda node: node.heuristic)
        self.ex = dict()
        self.heuristic = heuristic
    
    def add(self,child):
        child.heuristic = self.heuristic(child)
        self.F.add(child)
        self.ex[child.state] = 1
    
    def pick(self):
        return self.F.pop(0)
    
    def isEmpty(self):
        return not(self.F)

    def needExploring(self, state, depth):
        return not(state in self.ex)
    
    def getExplored(self):
        return len(self.ex) - self.getBorder()
    
    def getBorder(self):
        return len(self.F)
