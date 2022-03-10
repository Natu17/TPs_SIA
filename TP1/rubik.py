from ctypes import sizeof
import random
from shutil import move
solved = 'wwwwbbbbooooggggrrrryyyy'
MAX_DEPTH = 13

#Front rotation
def F(state):
    return (state[19]+state[1]+state[2]+state[18]+
    state[7]+state[4]+state[5]+state[6]+
    state[3]+state[0]+state[10]+state[11]+
    state[12]+state[13]+state[14]+state[15]+
    state[16]+state[17]+state[21]+state[22]+
    state[20]+state[8]+state[9]+state[23])

# Front' rotation
def Fc(state):
    return (state[9]+state[1]+state[2]+state[8]+
    state[5]+state[6]+state[7]+state[4]+
    state[21]+state[22]+state[10]+state[11]+
    state[12]+state[13]+state[14]+state[15]+
    state[16]+state[17]+state[3]+state[0]+
    state[20]+state[18]+state[19]+state[23])

#Right rotation
def R(state):
    return (state[0]+state[1]+state[6]+state[7]+
    state[4]+state[5]+state[22]+state[23]+
    state[11]+state[8]+state[9]+state[10]+
    state[2]+state[3]+state[14]+state[15]+
    state[16]+state[17]+state[18]+state[19]+
    state[20]+state[21]+state[12]+state[13])


#Right' rotation
def Rc(state):
    return (state[0]+state[1]+state[12]+state[13]+
    state[4]+state[5]+state[2]+state[3]+
    state[9]+state[10]+state[11]+state[8]+
    state[22]+state[23]+state[14]+state[15]+
    state[16]+state[17]+state[18]+state[19]+
    state[20]+state[21]+state[6]+state[7])

#Top rotation
def T(state):
    return (state[3]+state[0]+state[1]+state[2]+
    state[4]+state[9]+state[10]+state[7]+
    state[8]+state[13]+state[14]+state[11]+
    state[12]+state[17]+state[18]+state[15]+
    state[16]+state[5]+state[6]+state[19]+
    state[20]+state[21]+state[22]+state[23])

#Top' rotation
def Tc(state):
    return (state[1]+state[2]+state[3]+state[0]+
    state[4]+state[17]+state[18]+state[7]+
    state[8]+state[5]+state[6]+state[11]+
    state[12]+state[9]+state[10]+state[15]+
    state[16]+state[13]+state[14]+state[19]+
    state[20]+state[21]+state[22]+state[23])


actions = [F,Fc,R,Rc,T,Tc]
actionsName = ['F','F\'','R','R\'','T','T\'']
#actions = [{'name':'F','exec':F}]

def check(state):
    return state == solved


#scrumble for starting position
def scramble():
    state = solved
    moves = ''
    rand = 0
    for i in range(MAX_DEPTH):
        rand = random.randint(0,len(actions)-1)
        state = actions[rand](state)
        moves += actionsName[rand] + ' '
        #print(state)
    print(moves)
    return state

def whatAction(previous, now):
    solved = 1
    i = 0
    while (solved and i < len(actions)):
        if(actions[i](previous) == now):
            solved = 0
        i += 1
    return actionsName[i-1]

