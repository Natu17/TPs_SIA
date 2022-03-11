class Node:
    def __init__(self, state,parent = None, action = None):
        self.state = state
        self.parent = parent
        self.action = action
    
def search(root, actions, condition, pick):
    ex = set()
    F = [Node(root)]
    while F:
        node = pick(F)
        if(node.state in ex): continue
        ex.add(node.state)
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
                F.append(child)

dfs = lambda root,actions,condition: search(root,actions,condition, lambda F: F.pop())
bfs = lambda root,actions,condition: search(root,actions,condition, lambda F: F.pop(0))