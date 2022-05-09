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
        #structure[0] += 1  # add bias
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
            self.w.append(self.rng.uniform(-1,1,(
                self.structure[i+1], self.structure[i]+1))) # +1 for the bias

    def feedforward(self, input, with_values=False):
        H = []
        V = []

        H.append(np.append(input,self.bias))
        for layer in self.w:
            input = np.append(input,self.bias)
            V.append(input)
            h = np.dot(layer, input)
            H.append(h)
            input = self.activation(h)
        
        V.append(input)
        if with_values:
            return input, H, V
        return input

    def retropropagation(self, expected, H, V, lr):

        output = V[-1]

        l = self.activation_der(H[-1])*(expected - output)
        lambdas = [np.array(l).reshape(len(l), 1)]

        for i in range(len(self.w)-2, -1, -1):
            h = H[i+1]
            layer = self.w[i+1]
            gp = self.activation_der(h)
            lo = lambdas[-1]
            #gp = np.append(gp,1)
            l = gp*np.dot(lo.T, np.delete(layer, -1, axis=1)) #remove bias weight
            l = l.T
            #l = l[:-1]
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
        dist = (expected - output)
        return 0.5*np.sum(dist**2)

    def train(self, dataset, batch_size=1, target_error=0, epochs=math.inf, learning_rate=0.1, momentum=0, callback=None, epoch_callback=None):
        errors = []
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
                    output, H, V = self.feedforward(input, with_values=True)
                    _deltas = self.retropropagation(expected, H, V, learning_rate)
                    if deltas:
                        deltas += _deltas
                    else:
                        deltas = _deltas

                for i in range(len(self.w)):
                    deltas[i] += momentum*deltas_old[i]
                    self.w[i] += deltas[i]

                deltas_old = deltas

                if callback is not None:
                    callback(self)

            if epoch_callback is not None:
                epoch_callback(self)

            error = self.error(dataset)
            errors.append(error)
        return errors

def softmax(vector):
	e = np.exp(vector)
	return e / e.sum()
	

if __name__ == '__main__':
    x = np.array([-1, 0, 1])
    act,der = sigmoid_gen({})
    print(x)
    print(act(x))
    print(der(x))
