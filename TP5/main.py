from network import Network
import fonts as f
import numpy as np
from matplotlib import pyplot as plt
import pickle
import time


def main():

    font = f.f2

    dataset = np.array([x.flatten() for x in font])

    network = Network(structure=[35, 10, 2, 10, 35], activation="sigmoid")

    plt.subplot(1, 2, 1)
    plt.imshow(dataset[1].reshape(7, 5), cmap="binary")

    iteration = 0
    tmp = time.time()

    def callback(x):
        nonlocal iteration
        nonlocal tmp
        t = time.time()
        print("iter:", iteration, " time:", t-tmp)
        tmp = t
        iteration += 1

    network.train(dataset, max_iter=1000, callback=callback)

    # save network in network.pkl
    with open("weights.pkl", "wb") as file:
        pickle.dump(network.w, file)

    print(network.error(dataset))
    a = network.feedforward(dataset[1])

    plt.subplot(1, 2, 2)
    plt.imshow(a.reshape(7, 5), cmap="binary")
    plt.show()


if __name__ == '__main__':
    main()
