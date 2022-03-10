class Node:
    def __init__(self,state, parent = None):
        self.state= state
        self.parent = parent
    
    



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
                return
            if not(child.state in ex):
                F.append(child)

