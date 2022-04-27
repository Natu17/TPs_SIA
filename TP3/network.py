import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def step(x):
    return 0 if x < 0 else 1

def lineal(x):
    return x

activations = {'sigmoid': sigmoid, 'step': step, 'lineal': lineal}

class Network:

    def __init__(self, structure =[3,1],  activation = 'sigmoid'):
        self.structure = structure
        self.w = []
        self.activation = activations.get(activation)
    
    def randomize(self):
        self.w.append(np.random.rand((self.input)))

    def feedforward(self, input):
        return 1


    def training(self, dataset, epochs = 100, learning_rate = 0.1):
        input = np.random.choice(learning_rate)
        