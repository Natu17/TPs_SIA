import rubik
import heuristics
import search
import time
import json
import sys

config_path = sys.argv[1] if len(sys.argv)>1 else "config.json"

file = open(config_path)
config = json.load(file)

config.setdefault("algorithm","BFS")
config.setdefault("step",2)
config.setdefault("limit",5)
config.setdefault("heuristic","manhattan")
config.setdefault("max_depth",5)
config.setdefault("graphics", False)
config.setdefault("initial_state",rubik.scramble(config["max_depth"])[0])

heuristics = {"manhattan":heuristics.manhattanDistance, "dist3D": heuristics.dist3D, "rookie":heuristics.heurRookie, "cubes":heuristics.heurCubes}


initial_state = config.get("initial_state")
algorithm = config.get("algorithm")
heurisitic = heuristics[config.get("heuristic")]

print("algorithm " + config.get("algorithm"))
search.graphics = config.get("graphics")
start = time.time()
if not algorithm or algorithm=="BFS":
    solve = search.bfs( initial_state , rubik.actions, rubik.check)
elif algorithm == "DFS":
    solve = search.dfs( initial_state , rubik.actions, rubik.check)
elif algorithm == "DFSVL":
    solve = search.dfsvl( initial_state , rubik.actions, rubik.check,config.get("limit"),config.get("step"))
    print("limit " + str(config["limit"]))
    print("step " + str(config["step"]))
elif algorithm == "LH":
    solve = search.localHeuristic(initial_state, rubik.actions, rubik.check, heurisitic)
    print("heuristic " + config.get("heuristic"))
elif algorithm == "GH":
    solve = search.globalHeuristic(initial_state , rubik.actions, rubik.check, heurisitic)
    print("heuristic " + config.get("heuristic"))
elif algorithm =="A":
    solve = search.a(initial_state, rubik.actions, rubik.check, heurisitic)
    print("heuristic " + config.get("heuristic"))
end = time.time()

nodes = solve['nodes']
moves = ' '.join(map(lambda node: node.action, nodes))
states = ' '.join(map(lambda node: node.state, nodes))

print("states " + states )
print("moves " + moves)
print("Explored " + str(solve["explored"]))
print("Border " + str(solve["border"]))
print("time " + str(end - start))
print("depth " + str(solve["depth"]))

input("press enter to close...")
