import math
from typing_extensions import Self
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def step(x):
    return np.where(x > 0, 1, 0)


def lineal(x):
    return x


activations = {'sigmoid': sigmoid, 'step': step, 'lineal': lineal}


class Network:

    bias = 1

    # W[i][j][k] layer i, weight k, neuron j

    #W[i]:
        #  N1    N2  ...  Nn
        #  w1    w1  ...  w1
        #  w2    w2  ...  w2
        #  ...   ...  ...  ...
        #  wn    wn  ...  wn

    def __init__(self, structure=[3, 1],  activation='sigmoid', seed=1):
        structure[0] += 1  # add bias
        self.structure = structure
        self.activation = activations.get(activation)
        if seed != 0:
            np.random.seed(seed)
        self.randomize()

    def randomize(self):
        self.w = []
        for i in range(len(self.structure) - 1):
            self.w.append(np.random.randn(
                self.structure[i], self.structure[i+1]))

    def feedforward(self, input):
        self.H = []
        input = np.array(input + [self.bias])
        for i in range(len(self.w)):
            h = np.dot(input, self.w[i])
            self.H.append(h)
            input = self.activation(h)
        return input
        

    
    
    def retropropagation(self,data, output, n, lr):
        lamda = []
        x = sp.Symbol('x')
        for i in range(len(data)):
            lamda[i] = sp.diff(self.activation(self.H[i][n],x))*(data[i] - output[i])
            delta = lr*lamda[i]*self.activation(self.H[i][n])
            self.w[i][n] = self.w[i][n] + delta

        for i in reversed(range(len(self.w)-1)):
            aux = np.dot(lamda, self.w[i])
            for j in range(len(lamda)):
                lamda[j] = aux*sp.diff(self.activaiton(self.H[i][j],x))
                delta = lr*lamda[j]*self.activaiton(self.H[i][j])
                self.w[i][j] = self.w[i][j] + delta
        


    def training(self, dataset, epochs=100, learning_rate=0.1):
        error = 1
        while error > 0.001:
            input = np.random.choice(dataset)
            output = self.feedforward(input)
            self.retropropagation(input,output,np.size(input),learning_rate)
            error =  sum((math.dist(OUT,self.feedforward(IN))) )**2 for (IN,OUT) in dataset

        
        


def plot():
    network = Network([2, 3, 1], 'sigmoid', seed=0)

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    sample = [[i, j] for i in x for j in y]
    value = [network.feedforward(s)[0] for s in sample]

    x = [s[0] for s in sample]
    y = [s[1] for s in sample]
    plt.scatter(x, y, c=value)
    plt.show()
    
def plot_line():
    network = Network([2,1], 'step', seed=0)
    input = [1,0]

    m,a,c = network.w[0]

    line = lambda x: (m*x + c)/a
    x = np.linspace(-1,1,100)
    plt.plot(x, line(x))
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    #plot_line()
    plot()