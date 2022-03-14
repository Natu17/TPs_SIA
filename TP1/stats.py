import rubik, search, heuristics, time
from collections import defaultdict
import matplotlib.pyplot as plt
N = i = 100
depth = 7

heurs = {"manhattan":heuristics.manhattanDistance, "dist3D": heuristics.dist3D, "rookie":heuristics.heurRookie, "cubes":heuristics.heurCubes}

R = []

while i:
    i-=1
    results = dict()
    initial_state = rubik.scramble(depth)[0]
    start = time.time()
    bfs = search.bfs(initial_state, rubik.actions, rubik.check)
    end = time.time()
    results["bfs"] = (end-start, bfs["explored"], bfs["depth"])

    # start = time.time()
    # dfs = search.dfs(initial_state, rubik.actions, rubik.check)
    # end = time.time()
    # results["dfs"] = (end-start, dfs["explored"], dfs["depth"])

    # start = time.time()
    # dfsvl = search.dfsvl(initial_state, rubik.actions, rubik.check,5,3)
    # end = time.time()
    # results["dfsvl"] = (end-start, dfsvl["explored"], dfsvl["depth"])

    for h in heurs:
        # start = time.time()     
        # lh = search.localHeuristic(initial_state, rubik.actions, rubik.check, heurs[h])
        # end = time.time()
        # results[h + " " + "local"] = (end-start, lh["explored"], lh["depth"])


        # start = time.time()
        # gh = search.globalHeuristic(initial_state, rubik.actions, rubik.check, heurs[h])
        # end = time.time()
        # results[h + " " + "global"] = (end-start, gh["explored"], gh["depth"])

        start = time.time()
        a = search.a(initial_state, rubik.actions, rubik.check, heurs[h])
        end = time.time()
        results[h + " " + "A*"] = (end-start, a["explored"], a["depth"])
    
    R.append(results)


print("finished running algorithms. calculating...")
def addDicts(d1,d2):
    d = dict()
   


f = defaultdict(lambda: (0,0,0))
for d in R:
    for k in d:
        f[k] = (f[k][0] + d[k][0]/N, f[k][1] + d[k][1]/N, f[k][2] + d[k][2]/N)

print("algorithm,time,explored,depth")
for key in f:
    print(key + "," +"{:.2f}".format(f[key][0]) + ","+"{:.2f}".format(f[key][1]) + ","+"{:.2f}".format(f[key][2]))







plt.ioff()



figureT = plt.figure(figsize=(10,10))
y = list(map(lambda k: f[k][0], f))
plt.bar(f.keys(),y)
plt.ylabel('Time(ms)')
plt.title("Time")
plt.draw()
plt.savefig("time.png")

figureE = plt.figure(figsize=(10,10))
y = list(map(lambda k: f[k][1], f))
plt.bar(f.keys(),y)
plt.ylabel('Explored Nodes')
plt.title("Explored")
plt.draw()
plt.savefig("explored.png")

figureD = plt.figure(figsize=(10,10))
y = list(map(lambda k: f[k][2], f))
plt.bar(f.keys(),y)
plt.ylabel('Depth')
plt.title("Depth")
plt.draw()
plt.savefig("depth.png")

