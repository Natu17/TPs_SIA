from rubik import * 
import search

def dist3D(node):
    heuristic = 0
    for i in range(0,len(cubes)):
        heuristic += dist(node.state, i)
    return heuristic/4

def dist(state, i):
    cube = cubes[i]
    c1 = hash[''.join([solved[cube[0]],solved[cube[1]],solved[cube[2]]])]
    for j,cube in enumerate(cubes):
        c2 = hash[''.join([state[cube[0]],state[cube[1]],state[cube[2]]])]
        if c1 == c2: 
            return abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1]) + abs(positions[i][2] - positions[j][2])





def manhattanDistance(node):
    heuristic = 0
    for i in cubes:
        heuristic += manhBfs(node.state, i)
    return heuristic/4

def cubeCheck(state, cube):
    for i in cube:
        if state[i] != solved[i]:
            return False
    return True


def manhBfs(root, cube): 
    return search.bfs(root, actions, lambda state: cubeCheck(state,cube),True)["nodes"].pop().depth






def heurCubes(node):
    state = node.state
    total = 0
    for cube in cubes:
        if cubeCheck(state, cube):
            total += 1
    return (7-total)/4





def heurRookie(node):
    state = node.state 
    total = 0
    for i in range(0, len(state)):
        total += 1 if state[i]==solved[i] else 0
    return 21 - total 
