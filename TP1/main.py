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
    #solve = search.bfs( scramble[0] , rubik.actions, rubik.check)
    solve = search.dfsvl( scramble[0] , rubik.actions, rubik.check,1,1)
    end = time.time()
    print(solve)
    print(end - start)
