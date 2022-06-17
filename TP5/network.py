import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
# import tensorflow as tf
# from tensorflow.keras.optimizers import Adam


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


activations_gens = {'sigmoid': sigmoid_gen,
                    'step': step_gen, 'lineal': lineal_gen, 'tanh': tan_gen}


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
        # structure[0] += 1  # add bias
        self.structure = structure
        self.activation, self.activation_der = activations_gens.get(
            activation)(args)

        if seed != 0:
            self.rng = np.random.default_rng(seed)
        else:
            self.rng = np.random.default_rng()
        self.randomize()

    def randomize(self):
        self.w = []
        for i in range(len(self.structure) - 1):
            self.w.append(self.rng.uniform(-1, 1, (
                self.structure[i+1], self.structure[i]+1)))  # +1 for the bias

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

        for layer in self.w[start:end]:
            input = np.append(input, self.bias)
            h = np.dot(layer, input)
            input = self.activation(h)

        return input

    def error(self, dataset):
        expected = np.array([OUT for OUT in dataset])
        output = np.array([self.feedforward(IN) for IN in dataset])

        dist = (expected - output)
        #dist = np.linalg.norm(dist, axis=1)
        return 0.5*np.sum(dist**2)
        #return np.mean(dist)

    # def train(self, dataset, max_iter = math.inf, learning_rate = 0.1, beta1 = 0.9, beta2 = 0.999, epsilon = 1e-8):
    #     opt = Adam(learning_rate=learning_rate, beta_1=beta1, beta_2=beta2, epsilon=epsilon)
    #     this = self
    #     variables = [tf.Variable(v) for v in self.flatten()]

    #     def loss():
    #         this.reconstruct(variables)
    #         return this.error(dataset)
    #     iter = 0
    #     while(iter < max_iter):
    #         opt.minimize(loss, variables)
    #         iter+=1

    #     self.reconstruct(variables)
    #     return self

    def train(self, dataset,  learning_rate=0.1, max_iter=math.inf, callback=None):
        this = self

        def loss(flat):        
            this.reconstruct(flat)
            return this.error(dataset)       

        result = optimize.minimize(loss, np.array(
            self.flatten()), method='CG', callback=callback, options={'maxiter': max_iter})
        planar = result.x
        self.reconstruct(planar)


if __name__ == '__main__':
    pass
