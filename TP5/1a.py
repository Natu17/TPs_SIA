from network import Network
import fonts as f
import numpy as np
from matplotlib import pyplot as plt
import pickle
import time


def main():

    font = f.f2

    dataset = np.array([[x.flatten(), x.flatten()] for x in font])
    dataset = dataset[0:10]
    network = Network(structure=[35, 20, 2, 20, 35], activation=[
                       "relu","lineal","relu", "sigmoid"], seed=17)

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
        # plt.yscale("log")
        plt.pause(0.01)

    # network.train(dataset, max_iter=100, callback=callback)

    # plt.savefig("error.png")

    # #save network in network.pkl
    # with open("weights.pkl", "wb") as file:
    #     pickle.dump(network.w, file)

    #load weights
    with open("weights.pkl", "rb") as file:
        network.w = pickle.load(file)

    print(network.error(dataset))

    plt.figure("abc", figsize=(10, 100))

    for i,letter in enumerate(dataset):
        letter = letter[0]
        plt.subplot(len(dataset), 2, i*2+1)
        plt.imshow(letter.reshape(7, 5), cmap="binary")
        plt.subplot(len(dataset), 2, i*2+2)
        letter = network.feedforward(letter)
        plt.imshow(letter.reshape(7, 5), cmap="binary")
    plt.savefig("abc.svg")
    #plt.show()

    plt.figure("latent")
    data = np.array([network.encode(x[0]) for x in dataset])
    plt.scatter(data[:,0], data[:,1])
    plt.savefig("latent.svg")

    plt.figure("generate")
    encoded = network.encode(dataset[1][0])
    plt.subplot(1, 2, 1)
    plt.imshow(dataset[1][0].reshape(7, 5), cmap="binary")
    plt.subplot(1, 2, 2)
    encoded = encoded + np.random.normal(0,10, size=encoded.shape)
    decoded = network.decode(encoded)
    #decoded = np.where(decoded > 0.5, 1, 0)
    plt.imshow(decoded.reshape(7, 5), cmap="binary")
    plt.savefig("generate.svg")


if __name__ == '__main__':
    main()
