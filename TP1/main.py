import rubik
import search
import time


#rubik.depth()
#exit()
n = 1

while n:
    n = n - 1
    scramble = rubik.scramble()
    print(scramble) 
    start = time.time()
    solve = search.bfs( scramble[0] , rubik.actions, rubik.check)
    #solve = search.dfsvl( scramble[0] , rubik.actions, rubik.check,1,1)
    #solve = search.localHeuristic(scramble[0], rubik.actions, rubik.check, rubik.heuristic1)
    #solve = search.globalHeuristic( scramble[0] , rubik.actions, rubik.check, rubik.heurManDist)
    #solve = search.a(scramble[0], rubik.actions, rubik.check, rubik.heurManDist)
    end = time.time()
    
    nodes = solve['nodes']
    moves = ' '.join(map(lambda node: node.action, nodes))
    states = ' '.join(map(lambda node: node.state, nodes))

    print("states " + states )
    print("moves " + moves)
    print("Explored " + str(solve["explored"]))
    print("Border " + str(solve["border"]))
    print("time " + str(end - start))
    print("depth " + str(nodes.pop().depth))
