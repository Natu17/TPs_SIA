from network import Network
import fonts as f
import numpy as np
from matplotlib import pyplot as plt
import pickle
import time


def main():

    font = f.f2
    rng = np.random.RandomState(17)
    dataset = np.array([[x.flatten(), x.flatten()] for x in font])
    dataset = dataset[0:5]
    network = Network(structure=[35, 10, 2, 10, 35], activation=[
                       "relu","lineal","relu", "sigmoid"], seed=17)
    noise = []
    iters = 3
    for i in range(iters):
        for IN,OUT in dataset:
            IN += rng.normal(0, 0.1, IN.shape)
            noise.append([IN,OUT])

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
        errors.append(network.error(noise))
        plt.plot(errors)
        # plt.yscale("log")
        plt.pause(0.01)

    network.train(noise, max_iter=100, callback=callback)

    plt.savefig("error.png")

    # #save network in network.pkl
    with open("weights.pkl", "wb") as file:
        pickle.dump(network.w, file)

    #load weights
    # with open("weights.pkl", "rb") as file:
    #     network.w = pickle.load(file)

    print(network.error(noise))

    plt.figure("abc", figsize=(10, 100))

    for i,row in enumerate(noise):
        letter = row[0]
        expected = row[1]
        plt.subplot(len(noise), 3, i*3+1)
        plt.imshow(letter.reshape(7, 5), cmap="binary")
        plt.subplot(len(noise), 3, i*3+2)
        plt.imshow(expected.reshape(7, 5), cmap="binary")
        plt.subplot(len(noise), 3, i*3+3)
        letter = network.feedforward(letter)
        plt.imshow(letter.reshape(7, 5), cmap="binary")
    plt.savefig("abc.svg")
    #plt.show()

    plt.figure("latent")
    data = np.array([network.encode(x[0]) for x in noise])
    plt.scatter(data[:,0], data[:,1])
    plt.savefig("latent.svg")



if __name__ == '__main__':
    main()
