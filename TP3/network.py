import math
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_der(x):
    return (np.exp(-x))/((1+np.exp(-x))**2)


def step(x):
    return np.where(x > 0, 1, 0)


def step_der(x):
    return np.ones(x.shape)


def lineal(x):
    return x


def lineal_der(x):
    return np.ones(x.shape)


activations = {'sigmoid': (sigmoid, sigmoid_der), 'step': (
    step, step_der), 'lineal': (lineal, lineal_der)}


class Network:

    bias = 1

    # W[i][j][k] layer i, neuron j, weight k

    # W[i]:
    #  N1   w1, w2 ... wn           (e1)                e1*w1 + e1*w2 + ... + e1*wn
    #  N2   w1, w2 ... wn           (e2)                e2*w1 + e2*w2 + ... + e2*wn
    # .
    # .                                          =
    # .
    #  Nm   w1, w2 ... wn       *   (em)                em*w1 + em*w2 + ... + em*wn

    # mxn                    nx1                         mx1

    def __init__(self, structure=[3, 1],  activation='sigmoid', seed=1):
        structure[0] += 1  # add bias
        self.structure = structure
        self.activation, self.activation_der = activations.get(activation)

        if seed != 0:
            self.rng = np.random.default_rng(seed)
        else:
            self.rng = np.random.default_rng()
        self.randomize()

    def randomize(self):
        self.w = []
        for i in range(len(self.structure) - 1):
            self.w.append(self.rng.random((
                self.structure[i+1], self.structure[i])))

    def feedforward(self, input, with_exitations=False):
        H = []
        input = np.array(input + [self.bias])
        H.append(input)
        for layer in self.w:
            h = np.dot(layer, input)
            H.append(h)
            input = self.activation(h)
        if with_exitations:
            return input, H
        return input

    def retropropagation(self, expected, H, lr):

        output = self.activation(H[-1])

        V = [self.activation(h) for h in H]
        V[0] = H[0]

        l = self.activation_der(H[-1])*(expected - output)
        lambdas = [np.array(l).reshape(len(l), 1)]

        #self.w[-1] += lr * lambdas.reshape(len(lambdas),1) * V[-2].reshape(1,len(V[-2]))

        # for i in range(len(expected)):
        #     lamda[i] = V[-1][i]*(expected[i] - output[i])
        #     for k in range(len(H[i-1])):
        #         delta = lr*lamda[i]*self.activation(H[i-1][k])
        #         self.w[-1][i][k] = self.w[-1][i][k] + delta

        # for layer,H in reversed(zip(self.w[1:-1],H[1:-1])):
        for i in range(len(self.w)-2, -1, -1):
            h = H[i+1]
            layer = self.w[i+1]
            gp = self.activation_der(h)
            lo = lambdas[-1]
            l = gp*np.dot(lo.T,layer)
            l = l.T
            lambdas.append(l)

        for i in range(len(self.w)):
            l = lambdas[-i-1]
            v = V[i]
            self.w[i] += lr*l*v.reshape(1, len(v))

        # for i, layer in enumerate(reversed(self.w[:-1])):
        #     lambdas = self.w[-i-1]*lambdas.reshape(len(lambdas),1)
        #     lambdas = lambdas*self.activation_der(H[-2-i])
        #     self.w[-i-2] += lr*lambdas.T * V[-3-i].reshape(1,len(V[-3-i]))

        # for i in range(len(self.w)-1, 0,-1):
        #     aux = np.dot(self.w[i],lamda)
        #     for j in range(len(self.w[i])):
        #         lamda[j] = aux[j]*self.activation_der(H[i][j])
        #         for k in range(len(H[i-1])):
        #             delta = lr*lamda[j]*V[i-1][k]
        #             self.w[i][j][k] = self.w[i][j][k] + delta

    def train(self, dataset, epochs=100, learning_rate=0.1, callback=None):
        error = 1
        dataset = np.array(dataset, dtype=object)
        while error > 0.1:

            for input,expected in dataset:
                output, H = self.feedforward(input, with_exitations=True)
                self.retropropagation(expected, H, learning_rate)

                expected = np.array([OUT for IN, OUT in dataset])
                output = np.array([self.feedforward(IN) for IN, OUT in dataset])
                error = 0.5*np.sum(np.abs(expected - output)**2)
            print(error)

            if callback is not None:
                callback(self)


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
    network = Network([2, 1], 'step', seed=0)
    input = [1, 0]

    m, a, c = network.w[0][0]

    def line(x): return (m*x + c)/a
    x = np.linspace(-1, 1, 100)
    plt.plot(x, line(x))
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    plot_line()
    # plot()
