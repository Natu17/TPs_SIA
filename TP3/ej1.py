from network import Network
import numpy as np
import matplotlib.pyplot as plt


def a():
    dataset = [
        [[-1, -1], [-1]],
        [[-1, 1], [-1]],
        [[1, -1], [-1]],
        [[1, 1], [1]]
    ]

    network = Network(structure=([2, 1]), activation='step', seed=1)
    network.train(dataset)

    X = [x[0][0] for x in dataset]
    Y = [x[0][1] for x in dataset]
    c = [x[1][0] for x in dataset]

    plt.scatter(X, Y, c=c)

    m, a, b = network.w[-1][0]  # mx + ay + b = 0

    # y = -m*x + b

    x = np.linspace(-2, 2, 100)
    y = (-m*x - b)/a
    plt.plot(x, y)

    plt.show()


def b():
    dataset = [
        [[-1, -1], [-1]],
        [[-1, 1], [1]],
        [[1, -1], [1]],
        [[1, 1], [-1]]
    ]

    network = Network(structure=([2, 1]), activation='step', seed=1)
    network.train(dataset, learning_rate=1, epochs=1000)

    X = [x[0][0] for x in dataset]
    Y = [x[0][1] for x in dataset]
    c = [x[1][0] for x in dataset]

    plt.scatter(X, Y, c=c)

    m, a, b = network.w[-1][0]  # mx + ay + b = 0

    # y = -m*x + b

    x = np.linspace(-2, 2, 100)
    print(x[0])
    y = (-m*x - b)/a
    plt.plot(x, y)

    plt.show()


if __name__ == "__main__":
    b()
