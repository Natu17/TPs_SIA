import rubik
import algo
import time


#rubik.depth()
#exit()
n = 100

while n:
    n = n - 1
    scramble = rubik.scramble()
    print(scramble) 
    start = time.time()
    #solve = algo.bfs( scramble[0] , rubik.actions, rubik.check)
    solve = algo.dfsvl( scramble[0] , rubik.actions, rubik.check,5,3)
    end = time.time()
    print(solve)
    print(end - start)

