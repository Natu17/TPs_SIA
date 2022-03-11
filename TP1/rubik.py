import random
solved = 'wwwwbbbbooooggggrrrryyyy'
MAX_DEPTH = 10

class Action:
    def __init__(self, actionName, action):
        self.actionName = actionName
        self.action = action

#Front rotation
def F(state):
    return ''.join([state[19],state[1],state[2],state[18],
    state[7],state[4],state[5],state[6],
    state[3],state[0],state[10],state[11],
    state[12],state[13],state[14],state[15],
    state[16],state[17],state[21],state[22],
    state[20],state[8],state[9],state[23]])

# Front' rotation
def Fc(state):
    return ''.join([state[9],state[1],state[2],state[8],
    state[5],state[6],state[7],state[4],
    state[21],state[22],state[10],state[11],
    state[12],state[13],state[14],state[15],
    state[16],state[17],state[3],state[0],
    state[20],state[18],state[19],state[23]])

#Right rotation
def R(state):
    return ''.join([state[0],state[1],state[6],state[7],
    state[4],state[5],state[22],state[23],
    state[11],state[8],state[9],state[10],
    state[2],state[3],state[14],state[15],
    state[16],state[17],state[18],state[19],
    state[20],state[21],state[12],state[13]])


#Right' rotation
def Rc(state):
    return ''.join([state[0],state[1],state[12],state[13],
    state[4],state[5],state[2],state[3],
    state[9],state[10],state[11],state[8],
    state[22],state[23],state[14],state[15],
    state[16],state[17],state[18],state[19],
    state[20],state[21],state[6],state[7]])

#Top rotation
def T(state):
    return ''.join([state[3],state[0],state[1],state[2],
    state[4],state[9],state[10],state[7],
    state[8],state[13],state[14],state[11],
    state[12],state[17],state[18],state[15],
    state[16],state[5],state[6],state[19],
    state[20],state[21],state[22],state[23]])

#Top' rotation
def Tc(state):
    return ''.join([state[1],state[2],state[3],state[0],
    state[4],state[17],state[18],state[7],
    state[8],state[5],state[6],state[11],
    state[12],state[9],state[10],state[15],
    state[16],state[13],state[14],state[19],
    state[20],state[21],state[22],state[23]])


actions = [Action('F',F),Action('F\'',Fc),Action('R',R),Action('R\'',Rc),Action('T',T),Action('T\'',Tc)]

def check(state):
    return state == solved


#scrumble for starting position
def scramble():
    #return("gobybwbyorowgwbgryrwyrgo","SAMPLE")
    state = solved
    moves = ''
    rand = 0
    for i in range(MAX_DEPTH):
        rand = random.randint(0,len(actions)-1)
        state = actions[rand].action(state)
        moves += actions[rand].actionName + ' '
    return (state, moves)













import time

def get_moves(pos):
	return [F(pos),Fc(pos),R(pos),Rc(pos),T(pos),Tc(pos)]
def depth():
	start_time = time.time()
	dist = [{solved}, set(get_moves(solved))]
	while dist[-1]:
		dist.append(set())
		for pos in dist[-2]:
			for sub_pos in get_moves(pos):
				if sub_pos not in dist[-2] and sub_pos not in dist[-3]:
					dist[-1].add(sub_pos)
		print('Depth ' + str(len(dist) - 1) + ': ' + str(len(dist[-1])) + ' positions')
	print('2x2 Depth is ' + str(len(dist) - 2) + ', solved in ' + str(round(time.time() - start_time, 2)) + ' seconds')