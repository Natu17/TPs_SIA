solved = 'wwwwbbbbooooggggrrrryyyy'

#Front rotation
def F(state):
    return (state[19]+state[1]+state[2]+state[18]+
    state[7]+state[4]+state[5]+state[6]+
    state[3]+state[0]+state[10]+state[11]+
    state[12]+state[13]+state[14]+state[15]+
    state[16]+state[17]+state[21]+state[22]+
    state[20]+state[9]+state[9]+state[23])

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

    
