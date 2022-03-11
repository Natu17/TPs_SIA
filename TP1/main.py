import rubik
import algo
import time


#rubik.depth()
#exit()

while(True):
    scramble = rubik.scramble()
    print(scramble) 
    start = time.time()
    solve = algo.dfs( scramble[0] , rubik.actions, rubik.check)
    end = time.time()
    print(solve)
    print(end - start)

