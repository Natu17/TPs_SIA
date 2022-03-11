import rubik
import algo
import time


#rubik.depth()
#exit()
n = 10

while n:
    n = n - 1
    scramble = rubik.scramble()
    print(scramble) 
    start = time.time()
    solve = algo.dfslv( scramble[0] , rubik.actions, rubik.check,3,2)
    end = time.time()
    print(solve)
    print(end - start)

