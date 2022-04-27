import matplotlib.pyplot as plt
import numpy as np


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
        input = np.array(input + [self.bias])
        for i in range(len(self.w)):
            input = self.activation(np.dot(input, self.w[i]))
        return input

    def training(self, dataset, epochs=100, learning_rate=0.1):
        pass

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