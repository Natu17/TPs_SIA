import rubik
import algo
import time
solved = 'wwwwbbbbooooggggrrrryyyy'
#print(rubik.F(solved))
#print(rubik.T(solved))
#print(rubik.R(solved))
#print(rubik.Fc(solved))
#print(rubik.Tc(solved))
#print(rubik.Rc(solved))
#print(solved)
#rubik.scrumble()

scramble = rubik.scrumble()
print(scramble) 
start = time.time()
algo.dfs( scramble , rubik.actions, rubik.check)
end = time.time()
print(end - start)

