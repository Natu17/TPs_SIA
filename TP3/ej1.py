from network import Network
import numpy as np
import matplotlib.pyplot as plt

def plot(dataset, network):
    X = [x[0][0] for x in dataset]
    Y = [x[0][1] for x in dataset]
    c = [x[1][0] for x in dataset]

    plt.scatter(X, Y, c=c)

    m, a, b = network.w[-1][0]  # mx + ay + b = 0

    # y = -m*x + b

    x = np.linspace(-2, 2, 100)
    y = (-m*x - b)/a
    plt.plot(x, y)



def a():
    dataset = [
        [[-1, -1], [-1]],
        [[-1, 1], [-1]],
        [[1, -1], [-1]],
        [[1, 1], [1]]
    ]
    
    X = [x[0][0] for x in dataset]
    Y = [x[0][1] for x in dataset]
    c = [x[1][0] for x in dataset]
    x=np.linspace(-2,2,100)



    plt.scatter(X, Y, c=c)

    network = Network(structure=([2, 1]), activation='step', seed=0)
    
    line, = plt.plot(x,x)

    def callback(network):
        m, a, b = network.w[-1][0]  # mx + ay + b = 0

        # y = -m*x + b

        y = (-m*x - b)/a
        line.set_ydata(y)

        plt.savefig("tmo_{:08d}.png".format(callback.counter))
        callback.counter += 1
    callback.counter = 0    
    
    
    network.train(dataset, learning_rate=0.2)

    plt.figure("AND")
    plot(dataset, network)
    plt.savefig("AND.png")



def b():
    dataset = [
        [[-1, -1], [-1]],
        [[-1, 1], [1]],
        [[1, -1], [1]],
        [[1, 1], [-1]]
    ]

    network = Network(structure=([2, 1]), activation='step', seed=1)
    network.train(dataset, learning_rate=1, epochs=1000)

    plt.figure("XOR")
    plot(dataset, network)
    plt.savefig("XOR.png")

if __name__ == "__main__":
    a()
    #b()
