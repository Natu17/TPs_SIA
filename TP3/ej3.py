from network import Network
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 50)
y = np.linspace(0, 1, 50)
sample = [[i, j] for i in x for j in y]

def callback(network):

    plt.cla()
    value = [network.feedforward(s)[0] for s in sample]
    
    x = [s[0] for s in sample]
    y = [s[1] for s in sample]
    plt.scatter(x, y, c=value)
    plt.pause(0.01)

def a():

    dataset = [
        [[0,0], [0]],
        [[0,1], [1]],
        [[1,0], [1]],
        [[1,1], [0]]
    ]

    network = Network(structure=([2,2,1]), activation='sigmoid', seed=1)
    network.train(dataset, learning_rate=10)

    X = [ x[0][0] for x in dataset]
    Y = [ x[0][1] for x in dataset]
    c = [ x[1][0] for x in dataset]
    
    plt.scatter(X,Y,c=c)

    callback(network)

    plt.show()


    
    
if __name__ == "__main__":
    a()