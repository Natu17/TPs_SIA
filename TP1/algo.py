from collections import deque 
from graphics import update

graphics = True

class Node:
    def __init__(self, state,parent = None, action = None, depth=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth



def search(root, actions, condition, pick):
    r=Node(root)
    ex = dict()
    ex[root] = 1
    F = deque([r])
    while F:
        node = pick(F)
        state = node.state
        for action in actions:
            state = action.action(node.state)
            if not(state in ex): #Create Node AFTER state not explored check
                child = Node(state, node, action.actionName)
                if condition(state):
                    moves = ''
                    while(child):
                        if(child.action): moves = ''.join([child.action,moves])
                        child = child.parent
                    return moves
                ex[state] = 1
                F.append(child)
                if graphics: update(child)
    print('solution not found')

dfs = lambda root,actions,condition: search(root,actions,condition, lambda F: F.pop())
bfs = lambda root,actions,condition: search(root,actions,condition, lambda F: F.popleft())


def dfslv(root, actions, condition,limit,step):
    r = Node(root,None,None,0)
    ex = dict()
    F1 = deque([r])
    F2 = deque()
    while F1 or F2:

        if not(F1): 
            F = F1
            F1 = F2
            F2 = F
            limit += step
        node = F1.pop()
        state = node.state

        for action in actions:
            state = action.action(node.state)
            if not(state in ex): #Create Node AFTER state not explored check
                child = Node(state, node, action.actionName, node.depth+1)
                if condition(state):
                    moves = ''
                    while(child is not None):
                        if(child.action): moves = ''.join([child.action,moves])
                        child = child.parent
                    return state
                ex[state] = 1
                if child.depth > limit:
                    F2.append(child)
                else: F1.append(child)
                if graphics: update(child)



# def dfslv(root, actions, condition,limit,step):
#     r = Node(root,None,None,0)
#     ex = dict()
#     #ex[root] = 1
#     depth = 0
#     count = 0
#     F = deque([r])   
#     net.add_node(r)

#     while F:
#         if limit == count:
#             node = F.popleft()
#             if node.depth == limit:
#                 limit += step
#                 count = 0
#             else:
#                 count = limit
#         else: 
#             node = F.pop()
#             if node.depth == limit:
#               aux = F.popleft()
#               if aux is not None:
#                 if aux.depth == limit:
#                   limit += step
#                   count = 0
#                 F.append(node)
#                 node = aux    
#         state = node.state
        
#         count = count + 1
#         for action in actions:
#             state = action.action(node.state)
#             if not(state in ex): #Create Node AFTER state not explored check
#                 child = Node(state, node, action.actionName, node.depth+1)
#                 if condition(state):
#                     moves = ''
#                     while(child is not None):
#                         if(child.action is not None): moves = child.action + ' ' + moves
#                         child = child.parent
#                     return state
#                 ex[state] = 1
#                 F.append(child)
#                 update(child)
#     print('solution not found')