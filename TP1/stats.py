import rubik, search, heuristics, time
from collections import defaultdict
import matplotlib.pyplot as plt

progress=0
def plotStats(N,depth, heuris, algos, prefix,width=30,height=10):
    global progress
    heurs = {"manhattan":heuristics.manhattanDistance, "dist3D": heuristics.dist3D, "rookie":heuristics.heurRookie, "cubes":heuristics.heurCubes}
    i = N
    R = []

    progress = 0
    max = 3*N + 12*N + 1

    def incProgress():
        global progress
        print("\r"+str(int(100*progress/max))+"%            ", end="")
        progress +=1

    while i:
        i-=1
        results = dict()
        initial_state = rubik.scramble(depth)[0]
        
        if "bfs" in algos:
            start = time.time()
            bfs = search.bfs(initial_state, rubik.actions, rubik.check)
            end = time.time()
            results["bfs"] = (end-start, bfs["explored"], bfs["depth"])
        incProgress()

        if "dfs" in algos:
            start = time.time()
            dfs = search.dfs(initial_state, rubik.actions, rubik.check)
            end = time.time()
            results["dfs"] = (end-start, dfs["explored"], dfs["depth"])
        incProgress()

        if "dfsvl" in algos:
            start = time.time()
            dfsvl = search.dfsvl(initial_state, rubik.actions, rubik.check,5,3)
            end = time.time()
            results["dfsvl"] = (end-start, dfsvl["explored"], dfsvl["depth"])
        incProgress()

        for h in heurs:
            if h not in heuris:
                progress+=3
                continue
            if "lh" in algos:
                start = time.time()     
                lh = search.localHeuristic(initial_state, rubik.actions, rubik.check, heurs[h])
                end = time.time()
                results[h + " " + "local"] = (end-start, lh["explored"], lh["depth"])
            incProgress()

            if "gh" in algos:
                start = time.time()
                gh = search.globalHeuristic(initial_state, rubik.actions, rubik.check, heurs[h])
                end = time.time()
                results[h + " " + "global"] = (end-start, gh["explored"], gh["depth"])
            incProgress()

            if "a" in algos:
                start = time.time()
                a = search.a(initial_state, rubik.actions, rubik.check, heurs[h])
                end = time.time()
                results[h + " " + "A*"] = (end-start, a["explored"], a["depth"])
            incProgress()

            
        
        R.append(results)


    print("finished running algorithms. calculating...")
    def addDicts(d1,d2):
        d = dict()
    


    f = defaultdict(lambda: (0,0,0))
    for d in R:
        for k in d:
            f[k] = (f[k][0] + d[k][0]/N, f[k][1] + d[k][1]/N, f[k][2] + d[k][2]/N)

    # print("algorithm,time,explored,depth")
    # for key in f:
    #     print(key + "," +"{:.2f}".format(f[key][0]) + ","+"{:.2f}".format(f[key][1]) + ","+"{:.2f}".format(f[key][2]))







    plt.ioff()

    figureT = plt.figure(figsize=(width,height))
    y = list(map(lambda k: f[k][0], f))
    plt.bar(f.keys(),y)
    plt.ylabel('Time(ms)')
    plt.title("Time")
    plt.draw()
    plt.savefig(prefix + "time.png")

    figureE = plt.figure(figsize=(width,height))
    y = list(map(lambda k: f[k][1], f))
    plt.bar(f.keys(),y)
    plt.ylabel('Explored Nodes')
    plt.title("Explored")
    plt.draw()
    plt.savefig(prefix + "explored.png")

    figureD = plt.figure(figsize=(width,height))
    y = list(map(lambda k: f[k][2], f))
    plt.bar(f.keys(),y)
    plt.ylabel('Depth')
    plt.title("Depth")
    plt.draw()
    plt.savefig(prefix + "depth.png")


import os



for d in range(1,14):

    folder = "graphs/"+str(d) + "/"
    try:
        os.makedirs(folder)
    except:
        pass


    plotStats(10,d,["manhattan","dist3D","rookie","cubes"],["bfs","dfs","dfsvl","lh","gh","a"],folder + "all-")

    plotStats(10,d,["manhattan","dist3D","rookie","cubes"],["bfs","lh"],folder +"lh-",10)

    plotStats(10,d,["manhattan","dist3D","rookie","cubes"],["bfs","gh"],folder + "gh-",10)

    plotStats(10,d,["manhattan","rookie","cubes"],["bfs","gh"],folder + "gh-nodist-",10)

    plotStats(10,d,["manhattan","rookie","cubes"],["bfs","a"],folder + "A-",10)

    plotStats(10,d,["manhattan","rookie","cubes"],["bfs","dfsvl","a"],folder + "quick-",10)

#plotStats(10,50,[],["bfs","dfs"],"test",5)