import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_der(x):
    (np.exp(-x))/((1+np.exp(-x))**x)

def step(x):
    return np.where(x > 0, 1, 0)

def step_der(x):
    return 1
    
def lineal(x):
    return x

def lineal_der(x):
    return 1

activations = {'sigmoid': (sigmoid, sigmoid_der), 'step': (step, step_der), 'lineal': (lineal, lineal_der)}


class Network:

    bias = 1

    # W[i][j][k] layer i, neuron j, weight k

    #W[i]:
        #  N1   w1, w2 ... wn           (e1)                e1*w1 + e1*w2 + ... + e1*wn
        #  N2   w1, w2 ... wn           (e2)                e2*w1 + e2*w2 + ... + e2*wn
        # .     
        # .                                          =  
        # .
        #  Nm   w1, w2 ... wn       *   (em)                em*w1 + em*w2 + ... + em*wn

                #mxn                    nx1                         mx1

    def __init__(self, structure=[3, 1],  activation='sigmoid', seed=1):
        structure[0] += 1  # add bias
        self.structure = structure
        self.activation, self.activation_der = activations.get(activation)
        if seed != 0:
            np.random.seed(seed)
        self.randomize()

    def randomize(self):
        self.w = []
        for i in range(len(self.structure) - 1):
            self.w.append(np.random.randn(
                self.structure[i+1], self.structure[i]))

    def feedforward(self, input, with_exitations=False):
        H = []
        input = np.array(input + [self.bias])
        H.append(input)
        for layer in self.w:
            h = np.dot(layer, input)
            H.append(h)
            input = self.activation(h)
        return input, H if with_exitations else input
    
    def retropropagation(self,expected, H, lr):
        lamda = []
        output = self.activation(H[-1])

        V = self.activation(H)
        V[0] = H[0]


        # lambdas = self.activation_der(H[-1])*(expected - output)
        # self.w[-1] += lr * lambdas.reshape(len(lambdas),1) * V[-2].reshape(1,len(V[-2]))


        for i in range(len(expected)):
            lamda[i] = V[-1][i]*(expected[i] - output[i])
            for k in range(len(H[i-1])):
                delta = lr*lamda[i]*self.activation(H[i-1][k])
                self.w[-1][i][k] = self.w[-1][i][k] + delta

        H = H[:-1]
        V = V[:-1]
        # for layer, i in enumerate(reversed(self.w[:-1])):
        #     lambdas = lambdas*self.activation_der(H[-1-i])
        #     self.w[-1-i] += lr*lambdas.reshape(len(lambdas),1) * V[-2-i].reshape(1,len(V[-2-i]))
            

        for i in range(len(self.w)-1, 0,-1):
            aux = np.dot(self.w[i],lamda)
            for j in range(len(self.w[i])):
                lamda[j] = aux[j]*self.activation_der(H[i][j])
                for k in range(len(H[i-1])):
                    delta = lr*lamda[j]*V[i-1][k]
                    self.w[i][j][k] = self.w[i][j][k] + delta
        
        

    def training(self, dataset, epochs=100, learning_rate=0.1):
        error = 1
        while error > 0.001:
            input, expected = np.random.choice(dataset)
            output,H = self.feedforward(input, with_exitations=True)
            self.retropropagation(expected,output,H,learning_rate)
            
            error =  sum((math.dist(OUT,self.feedforward(IN)))**2 for (IN, OUT) in dataset)
           
        
        


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

    m,a,c = network.w[0][0]

    line = lambda x: (m*x + c)/a
    x = np.linspace(-1,1,100)
    plt.plot(x, line(x))
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    plot_line()
    #plot()