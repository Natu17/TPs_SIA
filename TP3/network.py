import math
import matplotlib.pyplot as plt
import numpy as np


def tan_gen(args):
    args.setdefault('b', 1)
    b = args['b']

    def activation(x):
        return np.tanh(b*x)

    def der(x):
        return b*(1-np.tanh(b*x)**2)

    return activation, der

def sigmoid_gen(args):
    args.setdefault('b', 1)
    b = args['b']

    def activation(x):
        return 1/(1+np.exp(-b*x))
    
    def der(x):
        return b*np.exp(-b*x)/(1+np.exp(-b*x))**2
    
    return activation, der

def step_gen(args):
    def activation(x):
        return np.where(x > 0, 1, -1)

    def der(x):
        return np.ones(x.shape)

    return activation, der


def lineal_gen(args):
    args.setdefault('b', 1)
    b = args['b']

    def activation(x):
        return b*x

    def der(x):
        return b*np.ones(x.shape)

    return activation, der


activations_gens = {'sigmoid':sigmoid_gen, 'step': step_gen, 'lineal': lineal_gen, 'tanh': tan_gen}


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

    def __init__(self, structure=[3, 1],  activation='sigmoid', seed=1, args={}):
        structure[0] += 1  # add bias
        self.structure = structure
        self.activation, self.activation_der = activations_gens.get(activation)(args)

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

        for i in range(len(self.w)-2, -1, -1):
            h = H[i+1]
            layer = self.w[i+1]
            gp = self.activation_der(h)
            lo = lambdas[-1]
            l = gp*np.dot(lo.T, layer)
            l = l.T
            lambdas.append(l)

        deltas = []
        for i in range(len(self.w)):
            l = lambdas[-i-1]
            v = V[i]
            delta = lr*l*v.reshape(1, len(v))
            deltas.append(delta)

        return deltas

    def error(self, dataset):
        dataset = np.array(dataset, dtype=object)
        expected = np.array([OUT for IN, OUT in dataset])
        output = np.array([self.feedforward(IN) for IN, OUT in dataset])
        return 0.5*np.sum(np.abs(expected - output)**2)

    def train(self, dataset, batch_size=1, target_error=0, epochs=math.inf, learning_rate=0.1, momentum=0, callback=None):
        if(len(dataset) % batch_size != 0):
            raise ValueError(
                "The dataset size must be a multiple of the batch size")
        error = 1
        dataset = np.array(dataset, dtype=object)
        batches_len = len(dataset) // batch_size

        deltas_old = [0 for _ in range(len(self.w))]

        while error > target_error and epochs > 0:
            epochs -= 1
            batches = self.rng.choice(dataset, size=(
                batches_len, batch_size), replace=False)

            for batch in batches:

                deltas = []

                for input, expected in batch:
                    output, H = self.feedforward(input, with_exitations=True)
                    _deltas = self.retropropagation(expected, H, learning_rate)
                    if deltas:
                        deltas += _deltas
                    else:
                        deltas = _deltas

                for i in range(len(self.w)):
                    self.w[i] += deltas[i] + momentum*deltas_old[i]
                    deltas_old = deltas

            error = self.error(dataset)
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
