import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


def tan_gen(args):
    args.setdefault('b', 1)
    b = args['b']

    def activation(x):
        return np.tanh(b*x)

    return activation


def sigmoid_gen(args):
    args.setdefault('b', 1)
    b = args['b']

    def activation(x):
        return 1/(1+np.exp(-b*x))

    return activation


def step_gen(args):
    def activation(x):
        return np.where(x > 0, 1, -1)

    return activation


def lineal_gen(args):
    args.setdefault('b', 1)
    b = args['b']

    def activation(x):
        return b*x

    return activation

def relu_gen(args):
    def activation(x):
        return np.where(x > 0, x, 0)

    return activation
    


activations_gens = {'sigmoid': sigmoid_gen,
                    'step': step_gen, 'lineal': lineal_gen, 'tanh': tan_gen, 'relu': relu_gen}


class Network:

    bias = 0.5

    # W[i][j][k] layer i, neuron j, weight k

    # W[i]:
    #  N1   w1, w2 ... wn           (e1)                e1*w1 + e1*w2 + ... + e1*wn
    #  N2   w1, w2 ... wn           (e2)                e2*w1 + e2*w2 + ... + e2*wn
    # .
    # .                                          =
    # .
    #  Nm   w1, w2 ... wn       *   (em)                em*w1 + em*w2 + ... + em*wn

    # mxn                    nx1                         mx1

    def __init__(self, structure=[3, 1],  activation=None, seed=1, args={}):
        # structure[0] += 1  # add bias
        self.structure = structure
        if not activation:
            activation = ["sigmoid" for i in range(len(structure)-1)]

        self.activation = [activations_gens[act](args) for act in activation]

        if seed != 0:
            self.rng = np.random.default_rng(seed)
        else:
            self.rng = np.random.default_rng()
        self.randomize()

    def randomize(self):
        self.w = []
        for i in range(len(self.structure) - 1):
            self.w.append(self.rng.uniform(-1, 1, (
                self.structure[i+1], self.structure[i])))  # +1 for the bias

    def flatten(self):
        flat = []
        for layer in self.w:
            flat.extend(layer.flatten())
        return flat

    def reconstruct(self, flat):
        w = []
        i = 0
        for layer in self.w:
            q = layer.size
            planar = np.array(flat[i:i+q])
            i += q
            w.append(planar.reshape(layer.shape))
        self.w = w
        return self.w

    def encode(self, input):
        return self.feedforward(input, end=len(self.structure)/2)

    def decode(self, input):
        return self.feedforward(input, start=len(self.structure)/2)

    def feedforward(self, input, start=0, end=None):

        if not end:
            end = len(self.structure)

        for i,layer in enumerate(self.w[start:end]):
            #input = np.append(input, self.bias)
            h = np.dot(layer, input)
            input = self.activation[i+start](h)

        return input

    def error(self, dataset):
        expected = np.array([OUT for OUT in dataset])
        output = np.array([self.feedforward(IN) for IN in dataset])

        dist = (expected - output)
        #dist = np.linalg.norm(dist, axis=1)
        return 0.5*np.sum(dist**2)
        #return np.mean(dist)


    def train(self, dataset,  learning_rate=0.1, max_iter=math.inf, callback=None):
        this = self

        def loss(flat):        
            this.reconstruct(flat)
            return this.error(dataset) + 0.1*np.max(flat**2)       

        result = optimize.minimize(loss, np.array(
            self.flatten()), method='Powell', callback=callback, options={'maxiter': max_iter})
        planar = result.x
        self.reconstruct(planar)

    

if __name__ == '__main__':
    pass
