from collections import deque 
class Node:
    def __init__(self, state,parent = None, action = None):
        self.state = state
        self.parent = parent
        self.action = action



def search(root, actions, condition, pick):
    #ex = set()
    ex = dict()
    ex[root] = 1
    F = deque([Node(root)])
    while F:
        node = pick(F)
        state = node.state
        #if(state in ex): continue
        #ex.add(node.state)
        #ex[state] = 1
        #print(len(ex))
        for action in actions:
            state = action.action(node.state)
            if not(state in ex): #Create Node AFTER state not explored check
                child = Node(state, node, action.actionName)
                if condition(state):
                    moves = ''
                    while(child is not None):
                        if(child.action is not None): moves = child.action + ' ' + moves
                        child = child.parent
                    return moves
                ex[state] = 1
                F.append(child)
    print('solution not found')

dfs = lambda root,actions,condition: search(root,actions,condition, lambda F: F.pop())
bfs = lambda root,actions,condition: search(root,actions,condition, lambda F: F.popleft())