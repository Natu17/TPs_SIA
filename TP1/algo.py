from multiprocessing import parent_process
from rubik import whatAction


class Node:
    def __init__(self, state,parent = None):
        self.state = state
        self.parent = parent
    
    



def bfs(root,actions, condition):
    ex = set()
    F = [Node(root)]
    
    while F:
        node = F.pop(0)
        if not(node.state in ex):
            ex.add(node.state)
            F.append(node)
            if(condition(node.state)):
                print(node.state)
                return
            for action in actions:
                #TODO check if childs are solved
                child = Node(action(node.state), node)
                if not(child.state in ex):
                    F.append(child)

def dfs(root,actions, condition):
    if condition(root):
            #Go up in the tree
            print(root)
            return
    ex = set()
    F = [Node(root)]
    
    while F:
        node = F.pop()
        ex.add(node.state)
        for action in actions:
            #TODO check if childs are solved
            child = Node(action(node.state), node)
            if condition(child.state):
                print(child.state)
                while(node is not None):
                    print(whatAction(node.state, child.state))
                    child = node
                    node = node.parent

                return
            if not(child.state in ex):
                F.append(child)
