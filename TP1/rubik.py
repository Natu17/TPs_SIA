
import random
import search

solved = 'wwwwbbbboooogggrrryyy'
cubes = ((0,5,16), (1,14,15), (2,10,13), (3,6,9), (4,17,18),(7,8,19),(11,12,20))
positions = ((0,1,1), (0,1,0), (1,1,0), (1,1,1), (0,0,1),(1,0,1),(1,0,0))


hash = {
    "rwb":0, "rbw":0, "wrb":0, "wbr":0,"bwr":0, "brw":0,
    "rwg":1, "rgw":1, "wrg":1, "wgr":1,"gwr":1, "grw":1,
    "owg":2, "ogw":2, "wog":2, "wgo":2,"gwo":2, "gow":2,
    "owb":3, "obw":3, "wob":3, "wbo":3,"bwo":3, "bow":3,
    "ryb":4, "rby":4, "yrb":4, "ybr":4,"byr":4, "bry":4,
    "oyb":5, "oby":5, "yob":5, "ybo":5,"byo":5, "boy":5,
    "oyg":6, "ogy":6, "yog":6, "ygo":6,"gyo":6, "goy":6,
}


class Action:
    def __init__(self, actionName, action):
        self.actionName = actionName
        self.action = action

#Front rotation
def F(state):
    return ''.join([state[17],state[1],state[2],state[16],
    state[7],state[4],state[5],state[6],
    state[3],state[0],state[10],state[11],
    state[12],state[13],state[14],
    state[15],state[18],state[19],
    state[8],state[9],state[20]])

# Front' rotation
def Fc(state):
    return ''.join([state[9],state[1],state[2],state[8],
    state[5],state[6],state[7],state[4],
    state[18],state[19],state[10],state[11],
    state[12],state[13],state[14],
    state[15],state[3],state[0],
    state[16],state[17],state[20]])

#Right rotation
def R(state):
    return ''.join([state[0],state[1],state[6],state[7],
    state[4],state[5],state[19],state[20],
    state[11],state[8],state[9],state[10],
    state[2],state[3],state[14],
    state[15],state[16],state[17],
    state[18],state[12],state[13]])

#Right' rotation
def Rc(state):
    return ''.join([state[0],state[1],state[12],state[13],
    state[4],state[5],state[2],state[3],
    state[9],state[10],state[11],state[8],
    state[19],state[20],state[14],
    state[15],state[16],state[17],
    state[18],state[6],state[7]])

#Top rotation
def T(state):
    return ''.join([state[3],state[0],state[1],state[2],
    state[4],state[9],state[10],state[7],
    state[8],state[13],state[14],state[11],
    state[12],state[15],state[16],
    state[5],state[6],state[17],
    state[18],state[19],state[20]])

#Top' rotation
def Tc(state):
    return ''.join([state[1],state[2],state[3],state[0],
    state[4],state[15],state[16],state[7],
    state[8],state[5],state[6],state[11],
    state[12],state[9],state[10],
    state[13],state[14],state[17],
    state[18],state[19],state[20]])


actions = [Action('F',F),Action('F\'',Fc),Action('R',R),Action('R\'',Rc),Action('T',T),Action('T\'',Tc)]

def check(state):
    return state == solved


#scrumble for starting position
def scramble(max_depth):
    state = solved
    moves = ''
    rand = 0
    for i in range(max_depth):
        rand = random.randint(0,len(actions)-1)
        state = actions[rand].action(state)
        moves += actions[rand].actionName + ' '
    return (state, moves)

