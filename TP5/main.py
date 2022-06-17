from network import Network
import fonts as f
import numpy as np
from matplotlib import pyplot as plt
import pickle
import time


def main():

    font = f.f2

    dataset = np.array([x.flatten() for x in font])
    dataset = dataset[0:10]
    network = Network(structure=[35, 15, 2, 15, 35], activation="relu")

    iteration = 0
    tmp = time.time()

    errors = []

    def callback(x):
        plt.figure("error")
        plt.clf()
        nonlocal iteration
        nonlocal tmp
        nonlocal errors
        nonlocal network
        t = time.time()
        print("iter:", iteration, " time:", t-tmp)
        tmp = t
        iteration += 1
        network.reconstruct(x)
        errors.append(network.error(dataset))
        plt.plot(errors)
        plt.yscale("log")
        plt.pause(0.01)

    network.train(dataset, max_iter=1000, callback=callback)

    # save network in network.pkl
    with open("weights.pkl", "wb") as file:
        pickle.dump(network.w, file)

    print(network.error(dataset))
    a = network.feedforward(dataset[1])

    plt.figure("a")
    plt.subplot(1, 2, 1)
    plt.imshow(dataset[1].reshape(7, 5), cmap="binary")
    plt.subplot(1, 2, 2)
    plt.imshow(a.reshape(7, 5), cmap="binary")
    plt.show()


if __name__ == '__main__':
    main()
