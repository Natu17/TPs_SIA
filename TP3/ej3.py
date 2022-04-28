from network import Network
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
sample = [[i, j] for i in x for j in y]


def callback(network):

    plt.cla()
    value = [network.feedforward(s)[0] for s in sample]

    x = [s[0] for s in sample]
    y = [s[1] for s in sample]
    plt.scatter(x, y, c=value, s=100)
    plt.pause(0.01)


def a():

    dataset = [
        [[-1, -1], [-1]],
        [[-1, 1], [1]],
        [[1, -1], [1]],
        [[1, 1], [-1]]
    ]

    network = Network(structure=(
        [2, 2, 1]), activation='tanh', seed=1, args={'b': 1})
    network.train(dataset, learning_rate=0.1, epochs=1000, momentum=0.9)
    print(network.error(dataset))
    X = [x[0][0] for x in dataset]
    Y = [x[0][1] for x in dataset]
    c = [x[1][0] for x in dataset]

    plt.scatter(X, Y, c=c)

    callback(network)

    plt.show()


if __name__ == "__main__":
    a()
